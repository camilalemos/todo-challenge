"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ToDoList.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/<str:description>',create_tasks),
    path('get/',get_tasks),
    path('delete/<int:id>',delete_task),
    path('complete/<int:id>',complete_task),
    path('filter_date_eq/<str:date>',filter_task_date_eq),
    path('filter_date_gt/<str:date>',filter_task_date_gt),
    path('filter_content/<str:content>',filter_task_content)
]
