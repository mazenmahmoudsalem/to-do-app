from django.db import models


class task(models.Model):
    title = models.CharField(max_length=50)
    date = models.IntegerField()
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.title
