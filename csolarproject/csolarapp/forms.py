from django import forms
from .models import Solar

class SolarForm(forms.ModelForm):
    class Meta:
        model=Solar
        fields=['name','desc','year','img']
