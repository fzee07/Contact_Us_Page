from django.contrib import admin
from django.urls import path

from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='Home'),
    path("about", views.about, name='About'),
    path("services", views.service, name='Services'),
    path("contacts", views.contacts, name='Contact')
]
