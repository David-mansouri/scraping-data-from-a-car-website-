# Generated by Django 3.2.5 on 2021-07-13 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Price',
            new_name='Deal',
        ),
    ]
