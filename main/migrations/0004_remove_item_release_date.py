# Generated by Django 3.2.21 on 2023-09-18 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_item_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='release_date',
        ),
    ]