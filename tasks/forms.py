from django import forms
from . import models


class add_task_form(forms.ModelForm):
    class Meta:
        model = models.task
        fields = ["title"]