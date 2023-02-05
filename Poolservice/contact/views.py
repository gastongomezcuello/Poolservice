from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import send_mail



# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = str(form.cleaned_data['name'])
            email = str(form.cleaned_data['email'])
            query = str(form.cleaned_data['query'])
            message = 'Nombre: ' + name + '\nCorreo electrónico: ' + email + '\nConsulta: ' + query
            subject = 'Contacto desde la web'
            form.save()
            send_mail(subject, message, 'poolservice.cba@gmail.com', ['poolservice.cba@gmail.com'])
            send_mail('Gracias por contactarte con nosotros', 'Hemos recibido tu consulta, en breve nos pondremos en contacto con vos', 'poolservice.cba@gmail.com', [email])

            return redirect('/')
        else:
            context = {'form': form}
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'contact/contact.html', context=context)