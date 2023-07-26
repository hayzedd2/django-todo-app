from django.shortcuts import render , redirect ,get_object_or_404
from . models import Task
from django.http import HttpResponse

# Create your views here.


def todo(request):
    incompleteTasks = Task.objects.filter(is_Completed = False).order_by('-updated_at') 
    completeTasks = Task.objects.filter(is_Completed = True).order_by('-updated_at') 
    
    Context = {
        'uncompleted' : incompleteTasks,
        'completed' : completeTasks
    }
    return render(request , "todoapp/home.html" , Context)


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('todo')

def markAsDone(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_Completed = True
    task.save()
    return redirect('todo')

def markAsUndone(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_Completed = False
    task.save()
    return redirect('todo')

def editTask(request , pk):
    getTask = get_object_or_404(Task , pk=pk)
    if request.method == 'POST':
        newTask = request.POST.get('task')
        getTask.task = newTask
        getTask.save()
        return redirect('todo')
    Context = {
        'getTask' : getTask
    }
    return render(request , "todoapp/edit.html" , Context)

def deleteTask(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.delete()
    return redirect('todo')