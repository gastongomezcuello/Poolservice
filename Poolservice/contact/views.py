from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import send_mail



# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail('Consulta', str(form.cleaned_data['query']), 'poolservice.cba@gmail.com', ['poolservice@gmail.com'])

            return redirect('/')
        else:
            context = {'form': form}
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'contact/contact.html', context=context)