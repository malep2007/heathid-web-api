# Generated by Django 2.1.7 on 2019-06-18 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20190618_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prefered_supplier',
            new_name='preferred_supplier',
        ),
    ]
