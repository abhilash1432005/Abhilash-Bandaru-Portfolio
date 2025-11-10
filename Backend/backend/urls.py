# Backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Backend.contact.urls')),   # <-- serve contact.home at '/'
]
