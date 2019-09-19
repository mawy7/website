from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def resources(request):
    context = {'nbar': 'resources'}
    template = 'resources.html'
    return render(request, template, context)