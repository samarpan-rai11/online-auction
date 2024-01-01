from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma
from product.models import Category, Product, Auction, Vendor


def index(request):
    products = Product.objects.filter(is_sold=False)
    auctions = Auction.objects.all()
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
