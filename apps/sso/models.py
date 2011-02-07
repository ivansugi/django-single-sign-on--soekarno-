from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Clients(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    url = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
        
class SessionControl(models.Model):
    
    id = models.CharField(max_length = 255, primary_key = True)
    client_token = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.id