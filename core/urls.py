from django.urls import path
from django.conf.urls import handler404
from . import views
from .views import custom_404_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('terms',views.terms, name='terms'),
]

handler404 = custom_404_view
