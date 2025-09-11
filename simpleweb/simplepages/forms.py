from django import forms

class SlideForm(forms.Form):
    title = forms.CharField(label="Slide Title", max_length=200)
    content = forms.CharField(widget=forms.Textarea, label="Slide Content")
