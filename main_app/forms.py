from django import forms
from .models import Sharpen

class SharpenForm(forms.ModelForm):
    class Meta: 
        model = Sharpen
        fields = ['date', 'sharp']