from django.db import models
from django.shortcuts import render
import datetime
from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

from captcha.fields import ReCaptchaField

# Create your models here.
class Contact(models.Model):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(required=True)

    def __str__(self):
        return self.name

