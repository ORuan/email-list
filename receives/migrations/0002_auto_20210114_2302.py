# Generated by Django 3.1.5 on 2021-01-14 23:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 1, 14, 23, 2, 7, 380802, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emailsthatwillreceive',
            name='created_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2021, 1, 14, 23, 2, 7, 381162, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('time_expires', models.TimeField()),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
