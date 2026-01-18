from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from todolistapp.models import *
from todolistapp.forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def homepage(request):
    context = {
        'page' : 'HomePage'
    }
    return render(request,"index.html",context)

@login_required
def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            instance = form_data.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, "Task added successfully.")
            return redirect("todolist")

    all_tasks = Task.objects.filter(owner=request.user)
    paginator = Paginator(all_tasks, 5)
    page = request.GET.get("page")
    all_tasks = paginator.get_page(page)

    context = {
        'page' : 'TaskList',
        'all_tasks' : all_tasks
    }
    return render(request,"todolist.html",context)

    # data={
    #     "name" : "Ayush",
    #     "location" : "Ghaziabad"
    # }
    # return JsonResponse(data)
    # return HttpResponse("<h1> this is my todolist. </h1>")

@login_required
def delete_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    if obj.owner == request.user:
        obj.delete()
        messages.success(request, f"Task {obj.task} deleted.")
    else:
        messages.error(request, "Not allowed.")
    return redirect("todolist")

@login_required
def edit_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    if request.method == "POST":
        form_data = TaskForm(request.POST or None,instance=obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task updated!!")
            return redirect("todolist")
        messages.success(request, "Error occurred in Task updation!!")
    else:
        context = {
            'obj' : obj
        }
        return render(request,"edit.html",context)
    
@login_required
def complete_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    if obj.owner == request.user:
        obj.is_completed = True
        obj.save()
        messages.success(request, "Status changed!!")
    else:
        messages.error(request, "Not allowed.")
    return redirect("todolist")

@login_required
def pending_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    if obj.owner == request.user:
        obj.is_completed = False
        obj.save()
        messages.success(request, "Status changed!!")
    else:
        messages.error(request, "Not allowed.")
    return redirect("todolist")

def contact(request):
    context = {
        'page' : 'Contact Page'
    }
    return render(request,"contact.html",context)

def about(request):
    context = {
        'page' : 'About Page'
    }
    return render(request,"about.html",context)
