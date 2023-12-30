from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('auction/<int:pk>/', views.auction_detail, name='auction_detail'),
    path('new/', views.new, name='new')
]