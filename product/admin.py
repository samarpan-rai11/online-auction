from django.contrib import admin
from .models import Category, Product, Auction, Bid, Auctioneer, Vendor, Order, CartOrder, Payment, UserProfile, ProductReview, CouponCode
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','price','on_stock']

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['categori','name','bid','on_stock','auction_status']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','address','contact','user']

class AuctioneerAdmin(admin.ModelAdmin):
    list_display = ['title','address','contact','user']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating']

class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ['code','discount']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid)
admin.site.register(Auctioneer, AuctioneerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Order)
admin.site.register(CartOrder)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(CouponCode, CouponCodeAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)


