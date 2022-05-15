from django.forms import ModelForm
from django import forms
from .models import Videos

class UploadForm(ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    class Meta:
        model = Videos
        fields = ['title','description']
        