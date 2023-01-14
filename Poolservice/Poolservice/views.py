from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
    