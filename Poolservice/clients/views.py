from django.shortcuts import render

from clients.models import Client
from clients.forms import ClientForm

# Create your views here.
def create_client(request):

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)
            context = {
                'message': 'Cliente creado correctamente'
            }
            
        else:
            context = {
                'form_errors': form.errors,
                'form': ClientForm()
            } 
    
    else:
        context = {
                'form': ClientForm()
            }          
    return render(request, 'clients/create-client.html', context=context)

def list_clients (request):
    clients = Client.objects.all()
    

    context = {
        'clients' : clients ,
       
    }
    return render (request, 'clients/clients.html', context=context)

    
    
