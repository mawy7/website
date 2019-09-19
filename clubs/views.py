from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def clubs(request):
    context = {'nbar': 'clubs'}
    template = 'clubs.html'
    return render(request, template, context)


def clubdetails(request):
    context = {'nbar': 'clubs'}
    template = 'clubdetails.html'
    return render(request, template, context)