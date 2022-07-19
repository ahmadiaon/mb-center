from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name' : 'Ahmadi',
        'nationality' : 'Indonesia'
    }
    # return HttpResponse('<h1>Hello Mitra Barito</h1>')
    return render(request, 'index.html', context)

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