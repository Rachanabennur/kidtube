import re
from django.shortcuts import redirect, render
from .models import Feed
from .forms import UploadForm

class Cards:
   def __init__(self, id, title, image, description):
        self.id = id
        self.title = title
        self.image = image
        self.description = description


    # return render(request,'home.html', cardsInfo)
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

def videoplay(request):
    cards = Feed.objects.all()
    return render(request, 'videoplay.html', context={"cards":cards})  


def AboutPageView(request):
    return render(request, 'about.html')
