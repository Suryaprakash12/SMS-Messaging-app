from django import forms 
from .models import Dialer

class Contact(forms.ModelForm):
    class Meta:
        model=Dialer
        fields=('name','phone')

class Message(forms.Form):
    body=forms.CharField()