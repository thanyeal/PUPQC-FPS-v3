# Generated by Django 5.0.6 on 2024-06-04 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceToTheCommunity',
            fields=[
                ('extension_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=200)),
                ('community', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('date_of_activity', models.CharField(max_length=50)),
                ('hours_completed', models.CharField(max_length=10)),
                ('extension_performance_score', models.IntegerField(default=0)),
                ('ext_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extensionservices', to='accounts.faculty')),
            ],
        ),
    ]
