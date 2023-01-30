from django.shortcuts import render, redirect



def index(request):

    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def faqs(request):
    return render(request, 'faqs.html', context={})

    
