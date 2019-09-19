from django.urls import path
from . import views

app_name = 'clubs'
urlpatterns = [
    path('', view=views.clubs, name='clubs'),
    path('/details', view=views.clubdetails, name='clubdetails'),
]