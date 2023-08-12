from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_management/task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_management/task_detail.html', {'task': task})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task-list'))
    else:
        form = TaskForm()
    return render(request, 'task_management/create_task.html', {'form': form})


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task-detail', args=[task_id]))
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_management/edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('task-list'))
