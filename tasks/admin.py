from django.contrib import admin
from .models import TaskTemplate
from .models import Task

admin.site.register(Task)
admin.site.register(TaskTemplate)