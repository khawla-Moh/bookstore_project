# Generated by Django 4.2 on 2024-05-24 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]