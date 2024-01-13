from django import forms

from .models import Product, Auction

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'image','tags']
        labels = {
            'category': 'Category',
            'title': 'Title',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
            'tags': 'Tags',
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 pr-6 rounded-xl'
            }),
            'tags': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class NewAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['categori', 'name', 'description', 'bid', 'image','duration','tags']
        labels = {
            'categori': 'Category',
            'name': 'Name',
            'description': 'Description',
            'bid': 'Opening Bid',
            'image': 'Image',
            'duration': 'Duration',
            'tags': 'Tags',
        }
        widgets = {
            'categori': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'bid': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 pr-6 rounded-xl'
            }),
            'duration': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'tags': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }



