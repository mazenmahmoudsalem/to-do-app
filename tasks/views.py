from django.shortcuts import render
from . import models


def home(request):
    tasks = models.task.objects.all()
    if request.GET.get("one"):
        task = models.task.objects.get(title=request.GET.get("one")[5:])
        task.delete()
    context = {"tasks": tasks}
    return render(request, "index.html", context)