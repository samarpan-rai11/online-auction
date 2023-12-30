from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
# from django.conf.urls.static import static

from .forms import LogInForm

app_name = 'userauth'

urlpatterns = [
    path('',views.home),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view, name='login'),
    path('logout',views.logout_view,name='logout')
]
