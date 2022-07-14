from email import message
import imp
import re
from turtle import title
from venv import create
from django import forms
from django.shortcuts import redirect, render
from .models import Feed, CommentClass, Feed1
from .forms import UploadForm, UploadForm1
from .AgeDetect import  predict_age_and_gender
from .comment_analysis import analysis
from Video_Classification.classify_nsfw_video import classify_video
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def HomePageView(request):
    cards = Feed1.objects.all()
    return render(request,'home.html', context={"cards": cards})


def index(request):
    return render(request, 'index.html')

def command(request, id):
    cards = Feed1.objects.all()
    for card in cards:
        if id == card["id"]:
            cards.remove(card)
    return render(request,'home.html', context={"cards": cards})

def upload2(request):
    context = {}
    context['form'] = Feed1()
    form= UploadForm1(request.POST,request.FILES)
    if request.method == "POST" :
            input_image = form['img'].value()
            input_vid = form['vid'].value()
            out_vid = str('../static/uploads/videos/')+ str(input_vid)
            out_image = str('../static/uploads/images/')+ str(input_image)
            op = str('D:\\Projects\\fyp\\kidtube\\project\\static\\uploads\\videos\\')+ str(input_vid)
            tags = classify_video(op)
            Feed1.objects.create(title = request.POST.get('title'), description = request.POST.get('description'), img = out_image, 
            vid = out_vid, category = request.POST.get('category'), tags = tags)
            return redirect(HomePageView)
        

    return render( request, "upload2.html", context={"form": UploadForm1})

# def upload(request):
#     if request.method == "POST" :
#             form = request.POST.get('')
#             inp = str(request.POST.get('vid'))
#             inp_image = str(request.POST.get('img'))
#             temp = inp.split('/')
#             op = str('D:\\Projects\\fyp\\kidtube\\project\\static\\uploads\\videos\\')+ str(temp[len(temp)-1])
#             tags = classify_video(op)
#             Feed.objects.create(title = request.POST.get('title'), description = request.POST.get('description'), img = inp_image, 
#             vid = inp, category = request.POST.get('category'), tags = tags, url = request.POST.get('url') )
#             return redirect(HomePageView)
        
#     return render(request,'upload.html', context={"form": UploadForm})

def videoplay(request, id):
    Comment=[]
    commentList = []
    safe_comment=[]
    for j in CommentClass.objects.all():
        if(str(j.video_id) == str(id)):
            commentList.append(j.message[2:-2])
     
    sel_card = Feed1.objects.get(id=id)
    flag=True
    cards = Feed1.objects.all()
    flag_age = True

    if request.method=="POST":
        comment=request.POST.get('comment')
        Comment.append(comment)
        safe_comment=analysis(Comment)
        commentList = []
        if(len(safe_comment)>0):
            CommentClass.objects.create(video_id = id, message = safe_comment)
        for j in CommentClass.objects.all():
            if(str(j.video_id) == str(id)):
                commentList.append(j.message[2:-2])
        

        return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card, "id":id, "flag":flag, "flag_age": flag_age, "commentList": commentList})
    if(sel_card.tags):
        flag = predict_age_and_gender()
        if flag == 0:
            flag_age = False
            return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card, "id" : id,"flag":flag, "flag_age": flag_age, "commentList": commentList})  

    return render(request, 'videoplay.html', context={"cards":cards, "sel_card":sel_card, "id" : id,"flag":flag, "flag_age": flag_age,"commentList": commentList})  




    

