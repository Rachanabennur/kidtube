from django.forms import ModelForm, ClearableFileInput
from django import forms
from .models import Feed

class UploadForm(ModelForm):    
    class Meta:
        model = Feed
        fields = ['title','description','img','vid','tag','category','url','comments']