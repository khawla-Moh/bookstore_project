# Generated by Django 4.2 on 2024-05-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher_date',
            new_name='publisher_year',
        ),
    ]