from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact/contact.html', context=context)