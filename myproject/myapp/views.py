from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = "ini nama orang"
    # return HttpResponse('<h1>Hello Mitra Barito</h1>')
    return render(request, 'index.html', {'name' : name})