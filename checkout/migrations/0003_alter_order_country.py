# Generated by Django 3.2.9 on 2021-12-02 06:52

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_original_bag_order_original_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=100),
        ),
    ]