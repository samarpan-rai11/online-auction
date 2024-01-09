from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display=['full_name', 'email', 'phone', 'subject']


admin.site.register(ContactUs, ContactUsAdmin)