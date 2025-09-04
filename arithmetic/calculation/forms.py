from django import forms

class CalculationForm(forms.Form):
    n1 = forms.IntegerField()
    n2 = forms.IntegerField()