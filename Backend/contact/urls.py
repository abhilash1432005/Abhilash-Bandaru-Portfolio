# Backend/contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # root -> home view (index.html)
    path('contact/', views.contact_view, name='contact'),  # POST contact handler
]
