from django.forms import ModelForm, ClearableFileInput
from django import forms
from .models import Videos, Feed

class UploadForm(ModelForm):    
    class Meta:
        model = Feed
        fields = ['title','description', 'long_desc', 'img','vid']
        widgets = {
            'media': ClearableFileInput(attrs={'multiple': True})
        }