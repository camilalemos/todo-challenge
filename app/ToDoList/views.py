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