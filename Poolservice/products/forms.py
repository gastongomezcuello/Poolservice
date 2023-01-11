from django import forms

class ProductForm(forms.Form):
    stock = forms.BooleanField(required=False)
    