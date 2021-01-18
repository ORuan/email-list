from django.forms import ModelForm
from django.contrib.auth.models import User
from receives.models import Campaign


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['name',
                  'start_data',
                  'end_data',
                  'hour_at_day',
                  'email_sender']
