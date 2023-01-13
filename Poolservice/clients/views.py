from django.shortcuts import render

from clients.models import Client
from clients.forms import ClientForm

# Create your views here.
def create_client(request):
    if request.method == 'GET':
        context = {
            'form': ClientForm()
        }       
        return render(request, 'clients/create-client.html', context=context)

    
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)
            context = {
                'message': 'Cliente creado correctamente'
            }
            return render(request, 'clients/create-client.html', context=context)
            
        else:
            context = {
                'form_errors': form.errors,
                'form': ClientForm()
            }
            return render(request, 'clients/create-client.html', context=context)
