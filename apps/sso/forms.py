from django.db import models
from django.forms import ModelForm

        
class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        

