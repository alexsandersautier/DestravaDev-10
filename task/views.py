from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required(login_url="/auth/login")
def tasks(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user)
    context = {"name": user.username, "tasks": tasks}
    return render(request, "tasks.html", context)

def finished(request):
    tasks = Task.objects.filter(id=request.POST.get('task_id')).first()
    tasks.completed = True
    tasks.save()
    return redirect("tasks")

@login_required(login_url="/auth/login")
def create(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        task = Task(description=description, user_id=request.user)
        task.save()
    return render(request, "task.html")