from django.urls import path
from . import views
from .views import custom_404_view

app_name = 'core'

urlpatterns = [
    #Home Page
    path('',views.index,name='index'),

    #Terms & Condition Page
    path('terms',views.terms, name='terms'),

    #Vendor List Page
    path('vendors/',views.vendor_list_view, name='vendor-list'),
]

handler404 = custom_404_view
