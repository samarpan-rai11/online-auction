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
    path('vendor-detail/<int:pk>/',views.vendor_detail, name='vendor-detail'),

]

handler404 = custom_404_view
