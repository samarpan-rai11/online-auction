from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma
from product.models import Category, Product
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm, LogInForm


def index(request):
    products = Product.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request,"index.html",{
        'categories': categories,
        'products': products,
    })


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)

def terms(request):
    return render(request, "terms.html")
