from django import forms
from product.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write a review...',
        'class': 'w-full py-4 px-6 rounded-xl',
        }))

    class Meta:
        model = ProductReview
        fields = ['review','rating']