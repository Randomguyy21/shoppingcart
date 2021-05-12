from django import forms
from .models import *
  
class ProductForm(forms.ModelForm):
  
    class Meta:
        model = Product
        fields = ['ProductName', 'Description', 'Image']

        widgets = {
            'ProductName': forms.TextInput(attrs={'class':'form-control'}),
            'Description': forms.TextInput(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control'}),
        }