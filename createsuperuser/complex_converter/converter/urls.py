from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_to_complex, name='convert_to_complex'),
]
from django.contrib import admin
from django.urls import path