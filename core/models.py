from django.db import models

# Create your models here.
class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta():
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.full_name
