from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Product, Auction, ProductReview, Vendor, Category
from .forms import NewProductForm
from core.forms import ProductReviewForm
from django.db.models import Q
from django.db.models.functions import Lower


# Create your views here.
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:4]

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
        'product': product,
        'average_rating': average_rating,
        'reviews': reviews,
        'make_review': make_review,
        'review_form': review_form,
        'related_products': related_products,
    })



def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    related_auctions = Auction.objects.filter(categori=auction.categori).exclude(pk=pk)[0:4]

    return render(request, 'product/auction_detail.html', {
        'auction': auction,
        'related_auctions': related_auctions,
    })



@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         product = form.save(commit=False)
    #         product.created_by = request.user
    #         product.save()

    #         return redirect('detail', pk=product.id)
    else:
        form = NewProductForm()

    return render(request, 'product/new.html', {
        'form': form,
        'title': 'New product',
    })


def shop_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)
    vendors = Vendor.objects.all()

    return render(request, 'product/shop.html',{
        'categories': categories,
        'products': products,
        'vendors': vendors,
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
    query = request.GET.get("q")
    categories = Category.objects.all()

    # you should use double underscores to navigate through the relationship and apply icontains to the related field
    products = Product.objects.filter(
    Q(title__icontains=query) |
    Q(description__icontains=query) |
    Q(tags__name__icontains=query)
    ).order_by("-date")


    return render(request,'product/search.html',{
        'categories': categories,
        'products': products,
        'query': query,
    })