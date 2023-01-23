from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form ,
                'error': 'Error al crear el usuario'
                }
            return render(request, 'users/signup.html', context=context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context=context)

    
