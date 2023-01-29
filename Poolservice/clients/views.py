from django.shortcuts import render
from clients.models import Client
from clients.forms import ClientForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
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
@login_required()
def list_clients (request):
    clients = Client.objects.all()
    queryset = request.GET.get('search')

    if queryset:
        clients = Client.objects.filter(
            Q(name__icontains = queryset) |
            Q(phone__icontains = queryset) 
        ).distinct()
    
    if len(clients) > 0:
        context = {
            'clients': clients,
        }
    else :
        context = {
            'message_clients': 'No se encontraron clientes'
        }   

    return render (request, 'clients/clients.html', context=context)

    
    
