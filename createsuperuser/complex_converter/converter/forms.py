from django import forms

class NumberForm(forms.Form):
    integer_number = forms.IntegerField(label="Enter an integer")
    float_number = forms.FloatField(label="Enter a float")
    complex_number = forms.CharField(label="Enter a complex number (e.g., 1+2j)")