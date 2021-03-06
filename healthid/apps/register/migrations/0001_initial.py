# Generated by Django 2.1.7 on 2019-04-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receipts', '0001_initial'),
        ('outlets', '0003_outlet_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('outlet', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='outlets.Outlet')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='receipttemplate', to='receipts.ReceiptTemplate')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
