from django.db import models
from django.urls import reverse


class Task(models.Model):
    description = models.CharField(max_length=100)
    time = models.IntegerField()
    person = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={'task_list_id': self.id})


