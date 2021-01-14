from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# Create your models here.
# For testingo-Dev
# sudo docker run --name postgres -e POSTGRES_PASSWORD=posgres -d postgres

class Campaign(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=False, unique=True)
    start_data = models.DateTimeField(null=False)
    end_data = models.DateTimeField(null=False)
    hour_at_day = models.TimeField(null=True)
    email_sender = models.EmailField(null=False)
    created_at = models.DateTimeField(auto_created=timezone.now())

class EmailsThatWillReceive(models.Model):
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    subject = models.CharField(max_length=40, null=False)
    name = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_created=timezone.now())

class Tokens(models.Model):
    token = models.UUIDField(default=uuid.uuid4)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    time_expires = models.TimeField(null=False)
    update_at = models.DateTimeField(auto_now_add=timezone.now())
    