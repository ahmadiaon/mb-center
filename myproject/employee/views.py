from tkinter.tix import Tree
from django.shortcuts import render
from django.http import HttpResponse

from employee.models import Employee



# Create your views here.
def index(request):
    return render(request, 'index.html')

def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees':employees})

def profile(request, pk):
    data_employee = Employee.objects.get(id=pk)
    context = {
        'name' : 'Ahmadi',
        'nationality' : 'Indonesia'
    }
    return render(request, 'profile_employee.html', {'data_employee':data_employee})