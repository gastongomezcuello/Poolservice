from django import forms

class ProductForm(forms.Form):
    code = forms.CharField(max_length=7 , label='Código')
    description = forms.CharField(max_length=85 , label='Descripción')
    tc2 = forms.CharField(max_length=4 , label='TC2')
    price = forms.FloatField(label='Precio')
    stock = forms.BooleanField(required=False, label='Stock')
    