from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LogInForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            username = signup_form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, Your account was created successfully.")
            return redirect('userauth:login')  # Redirect to your home page after signup
        
        if request.user.is_authenticated:
            return redirect('core:index')
    else:
        signup_form = SignUpForm()

    return render(request, 'userauth/signup.html', {
        'signup_form': signup_form,})



def login_view(request):
    if request.method == 'POST':
        login_form = LogInForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:index') #when using redirect use ('appname:name') and when render use .html file
            else:
                error_message = 'Invalid login credentials.'
        else:
            error_message = 'Invalid form submission.'
    else:
        login_form = LogInForm(request)
        error_message = None

    return render(request, 'userauth/login.html', {'login_form': login_form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    messages.success(request, "User is logged out.")
    return redirect("/")

        