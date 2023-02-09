from django.shortcuts import render, redirect
from clients.models import Client
from clients.forms import ClientForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def create_client(request,username):
    try:
        if request.user.profile != "NULL":
            return redirect('../../clients/complete-profile')
    except:
        client = Client(id=request.user.id, user=User.objects.get(username=username))
        new_client = client.save()
        return redirect('../../clients/complete-profile')
@login_required()
def update_client(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client.dni=form.cleaned_data['dni']
            client.cuit=form.cleaned_data['cuit']
            client.kind=form.cleaned_data['kind']
            client.phone=form.cleaned_data['phone']
            client.address=form.cleaned_data['address']
            client.city=form.cleaned_data['city']
            client.save()
            context = {
                'message': 'Cliente actualizado exitosamente'
            }
            return render(request, 'clients/complete-profile.html', context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ClientForm()
            }
            return render(request, 'clients/complete-profile.html', context)
    else:
        context = {
            'form': ClientForm(
                initial={
                    'dni': client.dni,
                    'cuit': client.cuit,
                    'kind': client.kind,
                    'phone': client.phone,
                    'address': client.address,
                    'city': client.city,
   
                }
            )
        }
        return render(request, 'clients/complete-profile.html', context)
    
    # if request.method == 'POST':
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         Client.objects.create(**form.cleaned_data)
    #         context = {
    #             'message': 'Cliente creado correctamente'
    #         }
            
    #     else:
            # context = {
            #     'form_errors': form.errors,
            #     'form': ClientForm()
            # } 
    
    # else:
    #     context = {
    #             'form': ClientForm()
    #         }          
    # return render(request, 'clients/create-client.html', context=context)
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

    
    
