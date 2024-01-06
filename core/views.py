from django.shortcuts import render, get_object_or_404
from product.models import Category, Product, Auction, Vendor, ProductReview
from django.db.models import Avg
from taggit.models import Tag
from django.http import JsonResponse


def index(request):
    products = Product.objects.filter(is_sold=False,).order_by("-date")[:4]
    auctions = Auction.objects.all().order_by("-date")[:4]
    categories = Category.objects.all()

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

