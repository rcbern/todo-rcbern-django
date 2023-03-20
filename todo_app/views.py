from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from todo_app.api import (all_task, get_task, filter_task, post_task, put_task,
                          upd_task, del_task)
from todo_app.models import Task
from todo_app.schema import TaskIn, TaskPut

__all__ = ['app', 'view_task', 'create_task', 'update_task', 'delete_task',
           'edit_task', 'submit_task', 'filter', 'save_task']


def app(request):
    tasks = all_task(request)
    return render(request, 'todo_app/tasks.html', {'tasks_list': tasks})


def view_task(request, task_id):
    task = get_task(request, task_id)
    return render(request, 'todo_app/task_detail.html', {'task': task})


def create_task(request):
    return render(request, 'todo_app/create_task.html')


def update_task(request, task_id):
    upd_task(request, task_id)
    return redirect('detail', task_id=task_id)


def delete_task(request, task_id):
    del_task(request, task_id)
    return redirect('home')


def edit_task(request, task_id):
    task = get_task(request, task_id)
    return render(request, 'todo_app/edit_task.html',  {'task': task})


@require_http_methods(['POST'])
def submit_task(request):
    data = {
        "task_name" : request.POST['task_name'],
        "task_category" : request.POST['task_category'],
        "task_description" : request.POST['task_description'],
        "date_completion" : request.POST['date_completion']
    }
    post_task(request, TaskIn(**data))
    return redirect('home')


@require_http_methods(['POST'])
def filter(request):
    filter_name = request.POST['task_filter']
    tasks = filter_task(request, filter_name)
    return render(request, 'todo_app/tasks.html', {'tasks_list': tasks})


@require_http_methods(['POST'])
def save_task(request, task_id):
    data = {
        "task_name" : request.POST['task_name'],
        "task_category" : request.POST['task_category'],
        "task_description" : request.POST['task_description'],
        "date_completion" : request.POST['date_completion']
    }
    put_task(request, task_id, TaskPut(**data))
    return redirect('detail', task_id=task_id)


# Create your views here.
