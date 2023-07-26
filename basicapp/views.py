from django.shortcuts import render  , get_object_or_404
from django.http import HttpResponse
from .models import employees
# Create your views here.

def view(request):
    return HttpResponse('first basic app')

def home(request):
    employee = employees.objects.all()
    Context = {
        'employee' : employee
    }
    return render(request , 'basicapp/index.html' ,  Context)

def detail(request , id):
    employee = get_object_or_404(employees , id=id)
    Context = {
        'employee' : employee
    }
    return render(request , "basicapp/detail.html" , Context)