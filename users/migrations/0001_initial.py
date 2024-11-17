# Generated by Django 5.1.3 on 2024-11-17 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('referral_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('referrer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referees', to='users.user')),
            ],
        ),
    ]
