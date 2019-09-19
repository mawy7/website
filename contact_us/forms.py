from django import forms
from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()

    