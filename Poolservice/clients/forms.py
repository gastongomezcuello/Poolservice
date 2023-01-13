from django import forms

class ClientForm(forms.Form):
    KIND_CHOICES = (
        ('Revendedor/a', 'Revendedor/a'),
        ('Cliente', 'Cliente'),        
    )

    name = forms.CharField(max_length=40 )
    kind = forms.ChoiceField(choices=KIND_CHOICES)
    email = forms.EmailField(max_length=40 )
    phone = forms.CharField(max_length=20 )
    address = forms.CharField(max_length=40 )
    city = forms.CharField(max_length=40 )
