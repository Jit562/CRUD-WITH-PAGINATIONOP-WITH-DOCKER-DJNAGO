from django import forms
from .models import Product
from django.core import validators

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pname', 'address', 'city', 'zip_code','mobile','date','message','is_true']

        widgets = {
            'pname': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        
        }