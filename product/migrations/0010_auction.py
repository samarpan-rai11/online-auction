# Generated by Django 4.2 on 2023-12-30 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0009_remove_product_duration_remove_product_product_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('bid', models.DecimalField(decimal_places=0, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='product_images')),
                ('on_stock', models.BooleanField(default=True)),
                ('categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='product.category')),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
