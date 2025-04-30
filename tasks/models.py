from django.db import models
from django.contrib.auth.models import User




class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class TaskTemplate(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title