from django.shortcuts import render, redirect
from.models import Task
# Create your views here.
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list') 
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})



def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')

    

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    messages.success(request, f'Task "{task.title}" updated!')
    return redirect('task_list')

def task_list(request):
    filter_option = request.GET.get('filter', 'all')  # domyślnie 'all'
    
    if filter_option == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_option == 'not_completed':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_option': filter_option})



    