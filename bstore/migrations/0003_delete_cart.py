# Generated by Django 4.0.6 on 2022-11-03 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bstore', '0002_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
    ]