from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)