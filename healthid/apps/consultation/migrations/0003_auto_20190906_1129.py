# Generated by Django 2.2 on 2019-09-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outlets', '0009_auto_20190710_0911'),
        ('business', '0004_auto_20190711_1004'),
        ('consultation', '0002_auto_20190801_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationcatalogue',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultation_catalogue', to='business.Business'),
        ),
        migrations.AddField(
            model_name='customerconsultation',
            name='outlet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outlet_consultations', to='outlets.Outlet'),
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
