from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.core.mail import send_mail
from .forms import ContactForm 
try:
    from django.urls import reverse
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import reverse  # pragma: no cover



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_subject = form.cleaned_data['subject']

            message = "Hello! {0} has sent you a new message from the Contact Page\n\nSender's Email:\n{1} \n\nMessage:{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail(sender_subject, message, sender_email, ['pyscholars@gmail.com'])
            return HttpResponseRedirect(reverse('contact_form_sent'))

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def get_success_url(self):
        # This is in a method instead of the success_url attribute
        # because doing it as an attribute would involve a
        # module-level call to reverse(), creating a circular
        # dependency between the URLConf (which imports this module)
        # and this module (which would need to access the URLConf to
        # make the reverse() call).
        return reverse('contact_form_sent')


