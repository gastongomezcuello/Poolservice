from django import forms

class ProductForm(forms.Form):
    Stock = forms.BooleanField(required=False)
    