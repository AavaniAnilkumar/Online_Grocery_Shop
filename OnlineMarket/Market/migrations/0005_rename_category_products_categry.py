# Generated by Django 4.1.2 on 2022-11-23 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0004_products_delete_fruits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Category',
            new_name='Categry',
        ),
    ]
