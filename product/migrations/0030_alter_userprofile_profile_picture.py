# Generated by Django 4.2 on 2024-01-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='user-default.png', null=True, upload_to='profile_pics/'),
        ),
    ]