# Generated by Django 4.1.2 on 2023-01-20 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarketWeb', '0011_cartdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cartdb',
            new_name='cartdetails',
        ),
    ]