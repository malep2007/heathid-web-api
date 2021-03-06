# Generated by Django 2.1.7 on 2019-07-30 14:49

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0010_auto_20190726_1023'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outlets', '0009_auto_20190710_0911'),
        ('events', '0004_auto_20190723_2132'),
        ('profiles', '0003_profile_loyalty_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('consultation_name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('approved_delivery_formats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[(0, 'In Person'), (1, 'Telephonic'), (2, 'Video Conferencing')], default=0, max_length=50), size=None)),
                ('consultant_role', models.IntegerField(choices=[(0, 'Doctor'), (1, 'Nurse'), (2, 'Health Coach'), (3, 'Pharmacist'), (4, 'Sales Associate')], default=3)),
                ('minutes_per_session', models.IntegerField()),
                ('price_per_session', models.IntegerField()),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outlets.Outlet')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerConsultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('consultant', models.CharField(blank=True, max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Now'), (1, 'Already Completed'), (2, 'Later')], default=0)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_by_user', to=settings.AUTH_USER_MODEL)),
                ('consultation_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_consultations', to='consultation.ConsultationCatalogue')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_event', to='events.Event')),
                ('sale_record', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation_sale_record', to='sales.Sale')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_consultation_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('medical_notes', models.TextField()),
                ('author', models.CharField(blank=True, max_length=50)),
                ('authorized_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_authorizations', to=settings.AUTH_USER_MODEL)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.CustomerConsultation')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='consultationcatalogue',
            unique_together={('consultation_name', 'outlet', 'approved_delivery_formats', 'minutes_per_session')},
        ),
    ]
