# farmmarketplace/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace_view, name=''),  # Map the root URL to the marketplace view
    # You can add more paths here for other views in your app.
]