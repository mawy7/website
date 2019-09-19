# contact_us/urls.py

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import contact_us

urlpatterns = [
	url(r'^$',
	        contact_us,
	        name='contact_us'),
	url(r'^sent/$',
        TemplateView.as_view(
            template_name='contact_form_sent.html'),
        name='contact_form_sent'),
]