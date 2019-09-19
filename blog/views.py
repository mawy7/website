from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def blog(request):
    context = {'nbar': 'blog'}
    template = 'blog.html'
    return render(request, template, context)