# Generated by Django 3.2.21 on 2023-09-12 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date_bought',
            new_name='release_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]
