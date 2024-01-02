from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='detail'),
    path('auction/<int:pk>/', views.auction_detail, name='auction_detail'),
    path('new/', views.new, name='new'),

    # add review
    path('add_review/<int:pk>', views.add_review, name='add_review')
]