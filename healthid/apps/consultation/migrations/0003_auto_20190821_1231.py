# Generated by Django 2.2 on 2019-08-21 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20190711_1004'),
        ('outlets', '0009_auto_20190710_0911'),
        ('consultation', '0002_auto_20190801_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationcatalogue',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerconsultation',
            name='outlet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='outlet_id', to='outlets.Outlet'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='consultationcatalogue',
            unique_together={('consultation_name', 'business', 'approved_delivery_formats', 'minutes_per_session')},
        ),
        migrations.RemoveField(
            model_name='consultationcatalogue',
            name='outlet',
        ),
    ]