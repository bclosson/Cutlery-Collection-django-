from django import forms
from .models import Sharpen, Cutlery

class SharpenForm(forms.ModelForm):
    class Meta: 
        model = Sharpen
        fields = ['date', 'sharp']

class CutleryForm(forms.ModelForm):
    class Meta:
        model = Cutlery
        fields = ('maker', 'style', 'use', 'steel', 'price')