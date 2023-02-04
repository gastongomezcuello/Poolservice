from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'description', 'tc', 'price', 'stock',]

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description','price', 'stock',]
    