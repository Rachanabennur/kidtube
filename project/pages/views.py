from re import template
from django.shortcuts import render
from django.views.generic import TemplateView


def HomePageView(request):
    titles = ['title1', 'title2']
    description = ['lorem ipsum for the first card description', 'lorem ipsum for the second card description']
    cardsInfo ={
        'data' : {'title1':'lorem ipsum for the first card description', 'title2':'lorem ipsum for the second card description'}
    }
    return render(request,'home.html', cardsInfo)

def AboutPageView(request):
    return render(request, 'about.html')