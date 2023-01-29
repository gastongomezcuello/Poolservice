from django.shortcuts import render, redirect
from contact.forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'contact/contact.html', context=context)