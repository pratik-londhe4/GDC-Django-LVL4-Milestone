# Add all your views here
from asyncio import tasks
from multiprocessing import context
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render

tasks = []
completed_task = []

def tasks_filter(task):
    if(task in completed_task):
        return True
    else:
        return False

if len(completed_task) > 0:
    tasks = filter(tasks_filter , tasks)


def tasks_view(request):
   
    return render(request , "tasks.html" , {"tasks" : tasks})



def add_task_view(req):
    task_value = req.GET.get("task")
    tasks.append(task_value)
                  
    return HttpResponseRedirect("/tasks")

def delete_task_view(req , index):
    del tasks[index-1]
    return HttpResponseRedirect("/tasks")


def complete_task_view(req , index):
    completed_task.append(tasks.pop(index-1))
    return HttpResponseRedirect("/tasks")


def completed_task_view(req):
    context = {
        
    }
    return render(req , "completed.html" , {"tasks" : completed_task})


def all_tasks_view(req):
    context = {
        "ptasks" : tasks,
        "ctasks" : completed_task
    }
    return render(req , 'index.html' , context)