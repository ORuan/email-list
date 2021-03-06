# Generated by Django 3.1.5 on 2021-01-12 19:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=datetime.datetime(2021, 1, 12, 19, 41, 42, 943576, tzinfo=utc))),
                ('name', models.CharField(max_length=40, unique=True)),
                ('start_data', models.DateTimeField()),
                ('end_data', models.DateTimeField()),
                ('hour_at_day', models.TimeField(null=True)),
                ('email_sender', models.EmailField(max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailsThatWillReceive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=datetime.datetime(2021, 1, 12, 19, 41, 42, 944084, tzinfo=utc))),
                ('active', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receives.campaign')),
            ],
        ),
    ]
