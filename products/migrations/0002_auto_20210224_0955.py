# Generated by Django 3.1.7 on 2021-02-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cateogry',
            new_name='category',
        ),
    ]
