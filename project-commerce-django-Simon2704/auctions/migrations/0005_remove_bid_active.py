# Generated by Django 4.1.3 on 2022-11-25 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='active',
        ),
    ]