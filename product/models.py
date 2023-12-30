from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images', default='default.png')

    class Meta():
        ordering = ('name',)
        verbose_name_plural = "Categories"

    #This makes django admin readable for category
    def __str__(self):   
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product_images', blank=True)
    
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    on_stock = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Auction(models.Model):
    categori = models.ForeignKey(Category, related_name='auctions', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bid = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='product_images', blank=True)

    made_by = models.ForeignKey(User, related_name='auction', on_delete=models.CASCADE)
    on_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name