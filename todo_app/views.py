from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods


from todo_app.models import Task

__all__ =['app','view_task','create_task','update_task','delete_task'
            ,'edit_task','submit_task','filter','save_task']

def app(request):
    tasks = Task.objects.all().order_by('date_completion')
    return render(request, 'todo_app/tasks.html', { 'tasks_list' : tasks})

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo_app/task_detail.html', {'task' : task})

def create_task(request):
    return render(request, 'todo_app/create_task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('detail', task_id = task_id)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todo_app/edit_task.html',  {'task' : task})

@require_http_methods(['POST'])
def submit_task(request):
    task_name = request.POST['task_name']
    task_category = request.POST['task_category']
    task_description = request.POST['task_description']
    date_completion = request.POST['date_completion']
    task = Task(
        task_name = task_name, 
        task_category = task_category, 
        date_completion = date_completion, task_description = task_description)
    task.save()
    return redirect('home')

@require_http_methods(['POST'])
def filter(request):
    filter_name = request.POST['task_filter']
    if filter_name == 'personal':
        tasks = Task.filters.personal()
    elif filter_name == 'work':
        tasks = Task.filters.work()
    else:
        tasks = Task.objects.all()
        return redirect('home')

    return render(request, 'todo_app/tasks.html', { 'tasks_list' : tasks })

@require_http_methods(['POST'])
def save_task(request, task_id):
    task = Task.objects.get(id=task_id)
    name = request.POST['task_name']
    category = request.POST['task_category']
    description = request.POST['task_description']
    completion = request.POST['date_completion']
    if name:
        task.task_name = name
    if description:
        task.task_description = description
    if completion:
        task.date_completion = completion
    task.task_category = category
    task.save()
    return redirect('detail', task_id = task_id)


# Create your views here.
