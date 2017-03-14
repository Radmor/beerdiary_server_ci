from django import forms
from .models import Pub

class PubForm(forms.ModelForm):
    class Meta:
        model = Pub