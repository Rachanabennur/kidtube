import re
from django.shortcuts import redirect, render
from .models import Videos, Feed
from .forms import UploadForm

class Cards:
   def __init__(self, id, title, image, description):
        self.id = id
        self.title = title
        self.image = image
        self.description = description

cards = [
     {
        "id": 1,
        "title": "Doctor Strange : Multiverse of Maddness",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Movies",
    },
    {
        "id": 2,
        "title": "KGF 2",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Movies",
    },
    {
        "id": 3,
        "title": "SpiderMan No Way Home",
        "image": "https://i.auto-bild.de/mdb/extra_large/99/2ergrantourer-a02.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Movies",
    },
    {
        "id": 4,
        "title": "National News Today",
        "image": "https://i.auto-bild.de/mdb/extra_large/99/2ergrantourer-a02.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"News",
    },
    {
        "id": 5,
        "title": "Software Project Management Tutorial",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Education",
    },
    {
        "id": 6,
        "title": "Software Engineering Tutorial",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Education",
    },
    {
        "id": 7,
        "title": "ICC Cricket WC ",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Sports",
    },
    {
        "id": 8,
        "title": "Thomas Cup Highlights",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Sports",
    },
    {
        "id": 9,
        "title": "Valorant Gaming Technique",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Gaming",
    },
    {
        "id": 10,
        "title": "Elephant farts on Human",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
        "category":"Comedy",
    },

  ]
    # return render(request,'home.html', cardsInfo)
def HomePageView(request):
    return render(request,'home.html', context={"cards": cards})


def index(request):
    return render(request, 'index.html')

def command(request, id):
    for card in cards:
        if id == card["id"]:
            cards.remove(card)
    return render(request,'home.html', context={"cards": cards})

def upload(request):
    form = UploadForm()
    if request.method == "POST" :
        form = UploadForm(request.POST, request.FILES)
        title = form.data["title"]
        print(title)
        desc = form.data["description"]
        print(desc)
        long_desc = form.data["long_desc"]
        print(long_desc)
        img = form.data["img"]
        print(img)
        vid = form.data["vid"]
        return redirect(HomePageView)
    return render(request,'upload.html', context={"form": UploadForm})


def AboutPageView(request):
    return render(request, 'about.html')
