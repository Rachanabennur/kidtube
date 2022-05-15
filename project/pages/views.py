from django.shortcuts import redirect, render
from .models import Videos
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
        "title": "Django Tutorial",
        "image": "data:image/png;base64,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",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
    },
    {
        "id": 2,
        "title": "Audi A1",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
    },
    {
        "id": 3,
        "title": "BMW 2er Gran Tourer",
        "image": "https://i.auto-bild.de/mdb/extra_large/99/2ergrantourer-a02.png",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
    },
    {
        "id": 4,
        "title": "Chevrolet Camaro",
        "image": "https://i.auto-bild.de/mdb/extra_large/53/fourthgeneration-439.jpg",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus aspernatur expedita placeat tempora quam! Nisi, similique, corrupti magnam unde tempore, necessitatibus aliquid illo nesciunt consequatur odit maxime voluptates voluptas illum.",
    },

  ]
    # return render(request,'home.html', cardsInfo)
def HomePageView(request):
      return render(request,'home.html', context={"cards": cards})


def command(request, id):
    for card in cards:
        if id == card["id"]:
            cards.remove(card)
    return render(request,'home.html', context={"cards": cards})

def upload(request):
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(HomePageView)
    return render(request,'upload.html', context={"form": UploadForm})


def AboutPageView(request):
    return render(request, 'about.html')

def LoginPageView(request):
    return render(request, 'registration/login.html')
