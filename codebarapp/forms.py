from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
 
    codebar = forms.CharField(label = '', widget=forms.TextInput(attrs={'class':'form-control required','required':''}))
    # create meta class
    class Meta:
        # specify model to be used
        model = Product
 
        # specify fields to be used
        fields = [
            "codebar",
            "productName",
            "brand",
            "ref",
        ]
        