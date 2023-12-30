from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Auction
from .forms import NewProductForm

# Create your views here.
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'product/detail.html', {
        'product': product,
        'related_products': related_products,
    })



def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    related_auctions = Auction.objects.filter(categori=auction.categori).exclude(pk=pk)[0:3]

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