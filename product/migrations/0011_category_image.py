# Generated by Django 4.2 on 2023-12-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='media/category_images/default.png', upload_to='category_images'),
        ),
    ]