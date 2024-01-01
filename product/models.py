from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.

AUCTION_DURATION = [
        (3, '3 days'),
        (5, '5 days'),
        (7, '7 days')
]

STATUS_CHOICE = (
    ('process','Processing'),
    ('shipped','Shipped'),
    ('delivered','Delivered')
)

RATING = (
    (1, "⭐️"),
    (2, "⭐️⭐️"),
    (3, "⭐️⭐️⭐️"),
    (4, "⭐️⭐️⭐️⭐️"),
    (5, "⭐️⭐️⭐️⭐️⭐️"),
)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images', default='default.png')

    class Meta():
        ordering = ('name',)
        verbose_name_plural = "Categories"

    #This makes django admin readable for category
    def __str__(self):   
        return self.name
    

class Vendor(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='vendor_images', blank=True)
    description = models.TextField(blank=True, null=True)

    address = models.CharField(max_length=100, default="1")
    contact = models.CharField(max_length=100, default="+123 456 789")

    authentic_rating = models.CharField(max_length=50, default="100")
    warrenty_period = models.CharField(max_length=50, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    image = models.ImageField(upload_to='product_images', blank=True)
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='vendor')
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    on_stock = models.BooleanField(default=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="in_review")

    date = models.DateTimeField(default=datetime.now,blank=True)
    update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_percent(self):
        new_price = (self.price/self.old_price)*100
        return new_price




class Auction(models.Model):
    categori = models.ForeignKey(Category, related_name='auctions', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bid = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product_images', blank=True)

    duration= models.PositiveIntegerField(choices=AUCTION_DURATION, blank=True, null=True)

    auction_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="in_review")
    made_by = models.ForeignKey(User, related_name='auction', on_delete=models.CASCADE)
    on_stock = models.BooleanField(default=True)

    date = models.DateTimeField(default=datetime.now,blank=True)
    update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE,related_name='bids')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder.username} - {self.bid_amount}"
    
    

########################## Order, Cart , Payment ###################
########################## Order, Cart , Payment ###################
########################## Order, Cart , Payment ###################


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    paid_status = models.BooleanField(default=False)

    order_date = models.DateTimeField(default=datetime.now,blank=True)
    order_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    order_time = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"



class CartOrder(models.Model):
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)

    invoice_no = models.CharField(max_length=100,default="001")
    item = models.CharField(max_length=200,default=0)
    image = models.CharField(max_length=200,default="")

    quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return f"{self.order.product} - {self.product.title}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    contact = models.CharField(max_length=70,default="+123 456 789", blank=True)

    def __str__(self):
        return self.user.username
    

######################## Product Review, Wishlist ##################
######################## Product Review, Wishlist ##################
######################## Product Review, Wishlist ##################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title