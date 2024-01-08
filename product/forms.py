from django import forms

from .models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'image']


