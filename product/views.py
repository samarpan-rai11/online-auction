from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.urls import reverse
from django.contrib import messages
from .models import Product, Auction, ProductReview, Vendor, Auctioneer, Category, Bids
from .forms import NewProductForm, NewAuctionForm
from core.forms import ProductReviewForm
from django.db.models import Q


# Create your views here.
def category_list(request):
    categories = Category.objects.all()

    return render(request, 'product/category-list.html', {
        "categories": categories,
    })


def category_list_p(request):
    categories = Category.objects.all()

    return render(request, 'product/category-list-p.html', {
        "categories": categories,
    })



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:4]

    vendors = Vendor.objects.all()

    #this means this product should be equal to ProductReview product field
    reviews = ProductReview.objects.filter(product=product).order_by("-date") 

    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    #product review form
    review_form = ProductReviewForm()
    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    return render(request, 'product/detail.html', {
        'p': product,
        'average_rating': average_rating,
        'reviews': reviews,
        'vendors': vendors,
        'make_review': make_review,
        'review_form': review_form,
        'related_products': related_products,
    })



# this function returns minimum bid required to place a user's bid
def minbid(min_bid, present_bid):
    for bids_list in present_bid:
        if min_bid < int(bids_list.bid):
            min_bid = int(bids_list.bid)
    return min_bid



def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    related_auctions = Auction.objects.filter(categori=auction.categori,live=True).exclude(pk=pk)[0:4]

    biddesc = Auction.objects.get(pk = pk, live = True)
    bids_present = Bids.objects.filter(listingid = pk)

    max_bid = minbid(biddesc.bid, bids_present)

    # auction.auction is used to access the related BidT object through the one-to-one relationship.
    bid_time= auction.auction
    end_time = bid_time.end_time if bid_time else None

    # In auction_detail view
    # winner_name = request.session.get('winner_name', None)


    try:
        winner_objects = Bids.objects.filter(bid=max_bid)  
        # Retrieve queryset of winner objects
        if winner_objects.exists():  
            # Check if there are any winner objects
            winner_object = winner_objects.first()  # Retrieve the first winner object from the queryset
            winner_name = winner_object.user
        else:
        # Handle the case where there are no winners
            winner_name = None
    
    except:
  
        winner_name = None


    return render(request, 'product/auction_detail.html', {
        'auction': auction,
        'related_auctions': related_auctions,
        'endingtime': end_time,
        "current_bid": minbid(biddesc.bid, bids_present),
        'winner_name': winner_name,
    })



def determine_winner(auct_id):
    try:
        # Get the user with the highest bid for the given listing
        winner_object = Bids.objects.filter(listingid=auct_id).order_by('-bid').first()
        winner_name = winner_object.user.username if winner_object else None
        return winner_name
    except Bids.DoesNotExist:
        return None


@login_required
def bids(request):
    bid_amnt = request.GET["bid_amnt"]
    try:
        auct_id = int(request.GET["auct_d"])
    except (KeyError, ValueError):
        return HttpResponse("Invalid or missing listing ID")


    bids_present = Bids.objects.filter(listingid = auct_id)
    startingbid = Auction.objects.get(pk = auct_id)
    min_req_bid = startingbid.bid
    min_req_bid = minbid(min_req_bid, bids_present)
    
    if int(bid_amnt) > int(min_req_bid):
        mybid = Bids(user = request.user, listingid = auct_id , bid = bid_amnt)
        mybid.save()

        winner_name = determine_winner(auct_id)

        messages.success(request, f"Congratulations, {request.user}! Your bid has been successfully placed. 🎉 Thank you for participating in the auction.")

        # storing the winner's name in the session
        request.session['winner_name'] = winner_name

        redirect_url = reverse('product:auction_detail', args=[auct_id])
    
        return redirect(redirect_url)
    else:
        messages.warning(request, f"Sorry, {request.user} ! Your bid should be higher than ${min_req_bid}.")

        return redirect(reverse('product:auction_detail', args=[auct_id]))
    
    return auction_detail(request, auct_id)



@login_required
def new(request):
    vendor_instance, created = Vendor.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = vendor_instance
            product.save()

            return redirect('product:detail', pk=product.id)
        else:
            print(form.errors)
    else:
        form = NewProductForm()

    return render(request, 'product/new.html', {
        'form': form,
        'title': 'New product',
    })



@login_required
def new_auction(request):
    auctioneer_instance, created = Auctioneer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = NewAuctionForm(request.POST, request.FILES)

        if form.is_valid():
            auction = form.save(commit=False)
            auction.auctioneer = auctioneer_instance
            auction.save()

            return redirect('product:auction_detail', pk=auction.id)
        else:
            print(form.errors)
    else:
        form = NewAuctionForm()

    return render(request, 'product/new_auction.html', {
        'form': form,
        'title': 'New auction',
    })



def shop_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False).order_by("-date")
    vendors = Vendor.objects.all()

    vendor_id = request.GET.get('vendor', 0)
    category_id = request.GET.get('category', 0)
    
    if vendor_id:
        products = products.filter(vendor_id=vendor_id)

    if category_id:
        products = products.filter(category_id=category_id)


    return render(request, 'product/shop.html',{
        'categories': categories,
        'products': products,
        'vendors': vendors,
        'category_id': int(category_id),
        'vendor_id': int(vendor_id),
    })



# this is for auction list page
def bid_view(request):
    categories = Category.objects.all()
    auctions = Auction.objects.filter(live=True).order_by("-date")
    auctioneers = Auctioneer.objects.all()

    auctioneer_id = request.GET.get('auctioneer', 0)
    category_id = request.GET.get('c', 0) # this c is what is used in loop in html
    
    if auctioneer_id:
        auctions = auctions.filter(auctioneer_id=auctioneer_id)

    if category_id:
        # this categori_id is generated by django as we created categori field in Auction class and django generated 'categori_id' because categori field is foreign key
        auctions = auctions.filter(categori_id=category_id)

    return render(request, 'product/bid.html',{
        'categories': categories,
        'auctions': auctions,
        'auctioneers': auctioneers,
        'category_id': int(category_id),
        'auctioneer_id': int(auctioneer_id),
    })



#this is form review form
def add_review(request,pk):
    product = Product.objects.get(pk=pk)
    user = request.user

    review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )

    average_reviews = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))

    return JsonResponse(
        {
        'bool': True,
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
        'average_reviews': average_reviews,
        }
    )



def search_view(request):
    query = request.GET.get('query', '')
    vendor_id = request.GET.get('vendor', 0)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    products = Product.objects.filter(is_sold=False).order_by("-date")


    if vendor_id:
        products = products.filter(vendor_id=vendor_id)

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {
        'products': products,
        'vendors': vendors,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'vendor_id': int(vendor_id),
    })



@login_required
def checkout_view(request):
    cart_total_price = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_price += int(item['qty']) * float(item['price'])

    return render(request, 'product/checkout.html',{
        "cart_data":request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj']),
        'cart_total_price': cart_total_price,
        })



@login_required
def payment_completed(request):
    cart_total_price = 0
    for p_id, item in request.session['cart_data_obj'].items():
            cart_total_price += int(item['qty']) * float(item['price'])
    context=request.POST
    return render(request, 'product/payment-completed.html',{
        "cart_data":request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj']),
        'cart_total_price': cart_total_price,
    })

