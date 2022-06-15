import imp
import re
from django.shortcuts import redirect, render
from .models import Feed
from .forms import UploadForm
from .AgeDetect import  predict_age_and_gender
from .comment_analysis import analysis

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
    Comment=[]
    safe_comment=[]
    sel_card = Feed.objects.get(id=id)
    print(sel_card.tags)
    flag=True
    cards = Feed.objects.all()
    if request.method=="POST":
        comment=request.POST.get('comment')
        print(comment)
        Comment.append(comment)
        safe_comment=analysis(Comment)

        # print(safe_co)
        return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card, "flag":flag, "safe_comment": safe_comment})
        
    if(sel_card.tags):
        flag = predict_age_and_gender()
    print(sel_card.title)
    return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card, "flag":flag, "safe_comment": safe_comment})  


def AboutPageView(request):
    return render(request, 'about.html')


def updateComment(request):
    if request.method == 'POSt':
        data = Feed.objects.get()
        data.comments = request.POST['commentlist']
        data.save()
    

