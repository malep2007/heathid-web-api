# Generated by Django 2.2 on 2019-11-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_supplierrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='supplier_order_number',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
    ]