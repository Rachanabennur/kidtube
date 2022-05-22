import re
from django.shortcuts import redirect, render
from .models import Feed
from .forms import UploadForm
from .AgeDetect import  predict_age_and_gender

def HomePageView(request):
    cards = Feed.objects.all()
    return render(request,'home.html', context={"cards": cards})


def index(request):
    return render(request, 'index.html')

def command(request, id):
    cards = Feed.objects.all()
    for card in cards:
        if id == card["id"]:
            cards.remove(card)
    return render(request,'home.html', context={"cards": cards})

def upload(request):
    form = UploadForm()
    if request.method == "POST" :
        form = UploadForm(request.POST)
        if form.is_valid() :
            form.save()
            print("Saved")
            return redirect(HomePageView)
        
    return render(request,'upload.html', context={"form": UploadForm})

def videoplay(request, id):
    sel_card = Feed.objects.get(id=id)
    print(sel_card.tags)
    print(sel_card.title)
    cards = Feed.objects.all()
    return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card})  


def AboutPageView(request):
    return render(request, 'about.html')

