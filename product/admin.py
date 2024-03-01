from django.contrib import admin
from .models import Category, Product, Auction, BidT, Auctioneer, Vendor, Order, Auction_Win, UserProfile, ProductReview, CouponCode, Bids, Winner
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','price','on_stock']

class AuctionAdmin(admin.ModelAdmin):
    list_display = ['categori','name','bid','live','auction_status']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','address','contact','user']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','paid_status', 'order_status', 'total_amount']

class Auction_WinAdmin(admin.ModelAdmin):
    list_display = ['auction','paid_status','total_amount']

class AuctioneerAdmin(admin.ModelAdmin):
    list_display = ['title','address','contact','user']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review','rating']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','contact','verified']

class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ['code','discount']

class BidTAdmin(admin.ModelAdmin):
    list_display = ['auction','end_time']

class BidsAdmin(admin.ModelAdmin):
    list_display = ['listingid','bid','user']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(BidT, BidTAdmin)
admin.site.register(Auctioneer, AuctioneerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Auction_Win)
admin.site.register(Winner)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CouponCode, CouponCodeAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Bids, BidsAdmin)


