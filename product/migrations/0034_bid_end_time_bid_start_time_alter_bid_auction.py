# Generated by Django 4.2 on 2024-01-11 07:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bid',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='product.auction'),
        ),
    ]