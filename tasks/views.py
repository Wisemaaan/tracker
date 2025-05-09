from django.shortcuts import render, redirect
from.models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import TaskCreateForm
from .forms import TaskEditForm





@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, user=request.user)
        if form.is_valid():

            
            selected_template = form.cleaned_data.get('template')
            manual_title = form.cleaned_data.get('title')

            if not selected_template and not manual_title:
                form.add_error('title', 'Musisz wpisać tytuł zadania lub wybrać z listy.')
                return render(request, 'tasks/add_task.html', {'form': form})

            task = form.save(commit=False)
            task.user = request.user

            if selected_template:
                task.title = selected_template.title
            else:
                task.title = manual_title  # ręczny tytuł

            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
    else:
        form = TaskCreateForm(user=request.user)

    return render(request, 'tasks/add_task.html', {'form': form})




@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskEditForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')

    
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    messages.success(request, f'Task "{task.title}" updated!')
    return redirect('task_list')


@login_required
def task_list(request):
    filter_option = request.GET.get('filter', 'all')  # domyślnie 'all'
    
    if filter_option == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_option == 'not_completed':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_option': filter_option})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'tasks/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
