"""
URL configuration for pandasapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alphas import views

# Define the URL patterns for your app
urlpatterns = [
    # The empty string '' path means this will be the home page of the app.
    # It will use the 'pandas_assignment' view from the views.py file.
    path('', views.pandas_assignment, name='pandas_assignment'),
]
