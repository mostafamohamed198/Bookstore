# Generated by Django 4.0.6 on 2022-11-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bstore', '0004_books_addtocart'),
    ]

    operations = [
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestedbooks', models.ManyToManyField(default=None, to='bstore.books')),
            ],
        ),
    ]
