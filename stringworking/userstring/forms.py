from django import forms

class UserString(forms.Form):
    str = forms.CharField()