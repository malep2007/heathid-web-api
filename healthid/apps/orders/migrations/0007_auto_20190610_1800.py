# Generated by Django 2.1.7 on 2019-06-10 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outlets', '0005_auto_20190523_1327'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_auto_20190529_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='destination_outlet',
        ),
        migrations.AddField(
            model_name='order',
            name='destination_outlet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='outlets.Outlet'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outlets.Outlet'),
        ),
    ]
