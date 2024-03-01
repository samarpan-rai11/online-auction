from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from product.models import Category, Product, Auction, Vendor, CouponCode, Order, UserProfile, Auction_Win
from core.models import ContactUs
from taggit.models import Tag
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    products = Product.objects.filter(is_sold=False,).order_by("-date")[:4]
    auctions = Auction.objects.filter(live=True).order_by("-date")[:4]
    categories = Category.objects.all()[:5]

    return render(request,"index.html",{
        'categories': categories,
        'products': products,
        'auctions': auctions,
    })



def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)



def terms(request):
    return render(request, "terms.html")



def vendor_list_view(request):
    vendors = Vendor.objects.all()
    vendor_count = vendors.count()

    return render(request,'vendor_list.html',{
        'vendors': vendors,
        'vendor_count': vendor_count,
    })



def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    products = Product.objects.filter(vendor=vendor).order_by("-date")

    return render(request, 'vendor_detail.html', {
        'vendor': vendor,
        'products': products,
    })



def tag_list(request,tag_slug=None):
    products = Product.objects.all().order_by('-id')

    tag = None

    # Check if a tag_slug is provided in the URL.
    if tag_slug:
        # If a tag_slug is provided, attempt to retrieve a Tag object with the specified slug from the database.
        tag = get_object_or_404(Tag,slug=tag_slug)

        # Filter the products to include only those associated with the retrieved tag.
        products = products.filter(tags__in=[tag])

    return render(request, 'tag.html',{
        'products': products,
        'tag': tag,
    })



# this is for adding products to cart button
def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        #if the product is in session
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        #if the product is not in session
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
            
    else:
        request.session['cart_data_obj'] = cart_product

    return JsonResponse({
        "data":request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj']),
        })


# cart list view
def cart_view(request):
    coupon = None
    valid_coupon = None
    invalid_coupon = None
    if request.method == "GET":
        coupon_code = request.GET.get('coupon-code')
        if coupon_code:
            try:
                coupon = CouponCode.objects.get(code = coupon_code)
                valid_coupon = "is applicable on Current Order"
            except:
                invalid_coupon = "Invalid coupon code"

    cart_total_price = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_price += int(item['qty']) * float(item['price'])
        return render(request, 'cart.html',{
            'cart_data':request.session['cart_data_obj'],
            'totalcartitems': len(request.session['cart_data_obj']),
            'cart_total_price': cart_total_price,
            'coupon': coupon,
            'valid_coupon': valid_coupon,
            'invalid_coupon': invalid_coupon,
        })
    else:
        messages.warning(request,"Your Cart is empty")
        return redirect('core:index')



# deleting from cart list page
def delete_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        #if the product is in session then this will delete the product
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
    
    cart_total_price = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_price += int(item['qty']) * float(item['price'])

    context = render_to_string("async/cart.html",{
        "cart_data":request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj']),
        'cart_total_price': cart_total_price,
        })
    
    #this 'data' is what is passed on js with #cart-list 
    return JsonResponse({
        'data':context,
        'totalcartitems':len(request.session['cart_data_obj']),
        })



# updating from the cart list page
def update_cart(request):
    product_id = str(request.GET['id'])
    qunatity = request.GET['qty'] #this gets from ajax code of js in object/dictionary which has 'data' key

    if 'cart_data_obj' in request.session:
        #if the product is in session then this will delete the product
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']

            #this will get the qunatity of the product and update it
            cart_data[str(request.GET['id'])]['qty'] = qunatity
            
            request.session['cart_data_obj'] = cart_data
        
    cart_total_price = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_price += int(item['qty']) * float(item['price'])

    context = render_to_string("async/cart.html",{
        "cart_data":request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj']),
        'cart_total_price': cart_total_price,
        })
    
    #this 'data' is what is passed on js with #cart-list 
    return JsonResponse({
        'data':context,
        'totalcartitems':len(request.session['cart_data_obj']),
        })


@login_required
def customer_dashboard(request):
    orders = Order.objects.filter(user=request.user)
    auction_win = Auction_Win.objects.filter(user=request.user)

    return render(request,'dashboard.html',{
        'orders':orders,
        'auction_wins':auction_win,
    })



@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request,'user-profile.html',{
        'profile': profile,
    })


def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request, 'user-edit.html',{
        'profile': profile,
    })



def contact(request):
    return render(request, 'contact.html')


def ajax_contact(request):
    # this variable is getting data from ajax in js
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name = full_name,
        email = email,
        phone = phone,
        subject = subject,
        message = message,
    )

    data={
        'bool': True,
        'message': "Message sent Successfully.",
    }

    return JsonResponse({"data": data})