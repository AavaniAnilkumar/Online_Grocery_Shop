# Generated by Django 4.1.2 on 2023-01-20 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarketWeb', '0015_rename_name_cartdb_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='Product',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='quantity',
            new_name='Quantity',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='total',
            new_name='Total',
        ),
    ]
