from django.forms import ModelForm, ClearableFileInput
from django import forms
from .models import Feed, Feed1

class UploadForm(ModelForm):    
    class Meta:
        model = Feed
        fields = ['title','description', 'img','vid','category','tags','url','comments']

class UploadForm1(ModelForm):    
    class Meta:
        model = Feed1
        fields = ['title','description', 'img','vid','category','tags']