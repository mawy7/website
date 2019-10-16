from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]


