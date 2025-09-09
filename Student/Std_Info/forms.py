from django import forms
from .models import StdInfo

class StdForm(forms.ModelForm):
    class Meta:
        model = StdInfo
        fields = ['std_name', 'std_age', 'std_city', 'std_email', 'std_phone_number', 'std_address']