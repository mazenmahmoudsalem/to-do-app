from django.db import models


class task(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True, auto_now_add=True)