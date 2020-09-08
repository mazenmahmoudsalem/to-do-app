from django.shortcuts import render, redirect
from . import models, forms


def home(request):
    tasks = models.task.objects.all()
    if request.GET.get("one"):
        task = models.task.objects.get(title=request.GET.get("one")[5:])
        task.delete()
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def add_task(request):
    form = forms.add_task_form()
    if request.method == "POST":
        form = forms.add_task_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("tasks:home")
    context = {"form": form}
    return render(request, "add_task.html", context)