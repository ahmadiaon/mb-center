from tkinter.tix import Tree
from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    context = {
        'name' : 'Ahmadi',
        'nationality' : 'Indonesia'
    }

    feature1 = Feature()
    feature1.id = 0
    feature1.name = "Fast"
    feature1.is_true = True
    feature1.details = "Our Service is Fast"

    feature2 = Feature()
    feature2.id = 1
    feature2.name = "Fast"
    feature2.is_true = True
    feature2.details = "Our Service is Fast"

    feature3 = Feature()
    feature3.id = 2
    feature3.is_true = True
    feature3.name = "Fast"
    feature3.details = "Our Service is Fast"
    
    feature4 = Feature()
    feature4.is_true = False
    feature4.id = 3
    feature4.name = "Fast"
    feature4.details = "Our Service is Fast"

    features = [feature1, feature2, feature3, feature4]



    # return HttpResponse('<h1>Hello Mitra Barito</h1>')
    return render(request, 'index.html', {'features' : features})

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'counter' : amount_of_words})

def profile(request):
    context = {
        'name' : 'Ahmadi',
        'nationality' : 'Indonesia'
    }
    return render(request, 'profile.html', context)