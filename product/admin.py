from django.contrib import admin
from .models import Category, Product, Auction
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','price','on_stock']

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['categori','name','bid','on_stock']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Auction, AuctionAdmin)

