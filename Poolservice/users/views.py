from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from clients.views import create_client
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required  

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form,                
            }
            return render(request, 'users/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'users/login.html', context=context)

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=user.username
            login(request, user)
            print('ACA LLEGA')
            return redirect(f'../../clients/create-client/{str(username)}')
            
        else:
            context = {
                'form': form ,
                'error': form.errors
                }
            print(form.errors)
            return render(request, 'users/signup.html', context=context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context=context)

    
