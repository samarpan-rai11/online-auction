from django import forms

from .models import Product

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'image','tags']
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
                'class': INPUT_CLASSES
            }),
            'tags': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }



