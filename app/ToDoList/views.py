from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from django.utils import dateformat   

from .models import *


# Create your views here.

def create_tasks(request,description):
    formatted_date = dateformat.format(datetime.now().date(), 'Y-m-d')
    print(str(formatted_date))
    task = Task(description=description,creation_date=formatted_date)

    task.save()
    return HttpResponse(task.id)

def get_tasks(request):
    tasks_list = Task.objects.all()
    return HttpResponse(tasks_list)

def delete_task(request, id):
    try:
        task = Task.objects.get(id = id)
        task.delete()
        return HttpResponse("Task deleted successfully!")
    except:
        return HttpResponse("Task doesn't exists")

def complete_task(request, id):
    try:
        task = Task.objects.get(id = id)
        task.completed=True
        task.save()
        return HttpResponse("Task completed successfully!")
    except:
        return HttpResponse("Task doesn't exists")
