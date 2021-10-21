from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from django.utils import dateformat   

from .models import *
from log import Logger

logger = Logger("ToDo_Log.log") 


def create_tasks(request,description):
    formatted_date = dateformat.format(datetime.now().date(), 'Y-m-d')
    task = Task(description=description,creation_date=formatted_date)

    task.save()
    logger.log_message(f"Created task {task.id} successfully")
    return HttpResponse(task.id)

def get_tasks(request):
    tasks_queryset = Task.objects.all()
    return HttpResponse(tasks_queryset)

def delete_task(request, id):
    try:
        task = Task.objects.get(id = id)
        logger.log_message(f"Deleted task {task.id} successfully")
        task.delete()
        return HttpResponse("Task deleted successfully!")
    except:
        logger.log_error("Task doesn't exists")
        return HttpResponse("Task doesn't exists")

def complete_task(request, id):
    try:
        task = Task.objects.get(id = id)
        task.completed=True
        task.save()
        logger.log_message("Task completed successfully!")
        return HttpResponse("Task completed successfully!")
    except:
        return HttpResponse("Task doesn't exists")

def filter_task_date_eq(request, date=None):
    return filter_task_date(request, date, True)

def filter_task_date_gt(request, date=None):
    return filter_task_date(request, date, False)

def filter_task_date(request, date, cmp):
    try:
        formatted_date = datetime.strptime(date, '%Y%m%d')
        tasks_list = list(Task.objects.all())
        if cmp:
            tasks_list = list(Task.objects.filter(creation_date=formatted_date))
        else:
            tasks_list = [task for task in tasks_list if task.creation_date.timestamp() >= formatted_date.timestamp()]

        return HttpResponse(tasks_list)

    except Exception as e:
        logger.log_error(f"Error: {str(e)}")
        return HttpResponse("Invalid Date")

def filter_task_content(request, content=None):
    tasks_list = Task.objects.filter(description__icontains=content.strip())
    logger.log_message("Filtered successfully")
    return HttpResponse(tasks_list)
