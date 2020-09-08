from django.shortcuts import render, redirect
from . import models, forms
import datetime


def home(request):
    if request.GET.get("done"):
        task = models.task.objects.get(title=request.GET.get("done")[5:])
        task.is_ended = True
        task.save()
    if request.GET.get("undone"):
        task = models.task.objects.get(title=request.GET.get("undone")[7:])
        task.is_ended = False
        task.save()
    if request.GET.get("delete"):
        task = models.task.objects.get(title=request.GET.get("delete")[7:])
        task.delete()
    tasks = models.task.objects.all()
    for task in tasks:
        if int(task.date) != int(datetime.datetime.now().strftime("%w")):
            if task.is_ended == True:
                task.delete()
    tasks = models.task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def add_task(request):
    if request.method == "POST":
        form = forms.add_task_form(request.POST)
        if form.is_valid():
            nform = form.save(commit=False)
            nform.date = int(datetime.datetime.now().strftime("%w"))
            nform.save()
            return redirect("tasks:home")
    form = forms.add_task_form()
    context = {"form": form}
    return render(request, "add_task.html", context)


def update_task(request, id):
    task = models.task.objects.get(id=id)
    if request.method == "POST":
        form = forms.add_task_form(request.POST, instance=task)
        if form.is_valid():
            nform = form.save(commit=False)
            nform.date = int(datetime.datetime.now().strftime("%w"))
            nform.save()
            return redirect("tasks:home")
    form = forms.add_task_form(instance=task)
    context = {"form": form}
    return render(request, "update_task.html", context)