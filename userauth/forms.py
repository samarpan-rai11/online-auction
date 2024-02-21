from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from product.models import UserProfile, Auctioneer, Vendor

class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Your Password'
    }))
    
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('auctioneer', 'Auctioneer'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'font-semibold text-[#0f2e40] p-2'
    }), required=True)


    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        if user_type not in ['customer', 'vendor', 'auctioneer']:
            raise forms.ValidationError("Select 'Customer', 'Vendor' or 'Auctioneer'.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        user_type = self.cleaned_data['user_type']
        profile, created = UserProfile.objects.get_or_create(user=user)

        if user_type == 'vendor':
            title = user.username
            Vendor.objects.create(user=user, title=title)
            profile.is_vendor = True
        elif user_type == 'auctioneer':
            title = user.username
            Auctioneer.objects.create(user=user, title=title)
            profile.is_auctioneer = True
        elif user_type == 'customer':
            profile.is_customer = True

        # Save the changes to the UserProfile
        profile.save()

        return user
