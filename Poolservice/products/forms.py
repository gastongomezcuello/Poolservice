from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'description', 'tc', 'price', 'stock',]

# class ProductForm(forms.Form):
#     code = forms.CharField(max_length=7 , label='Código')
#     description = forms.CharField(max_length=85 , label='Descripción')
#     tc2 = forms.CharField(max_length=4 , label='TC2')
#     price = forms.FloatField(label='Precio')
#     stock = forms.BooleanField(required=False, label='Stock')
    