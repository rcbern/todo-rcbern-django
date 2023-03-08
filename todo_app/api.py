from datetime import date
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema
from todo_app.models import Task


api = NinjaAPI()

class TaskIn(Schema):
    task_name: str
    task_description: str
    task_category: str = 'Personal'
    is_completed: bool = False
    date_completion: date
    date_creation: date

class TaskOut(Schema):
    id : int
    task_name: str
    task_description: str
    task_category: str
    is_completed: bool
    date_completion: date
    date_creation: date

@api.get('/all', response=list[TaskOut])
def all_task(request):
    task_temp = Task.objects.all()
    return task_temp

@api.get('/get', response=TaskOut)
def get_task(request, task_id:int):
    task_temp = get_object_or_404(Task, id = task_id)
    return task_temp

@api.post('/post', response=TaskOut)
def post_task(request, payload: TaskIn):
    task_temp = Task.objects.create(**payload.dict())
    return task_temp

@api.put('/put')
def update_task(request, task_id: int,payload: TaskIn):
    task_temp = get_object_or_404(Task, id = task_id)
    for key, value in payload.dict().items():
        setattr(task_temp, key, value)
    task_temp.save()
    return {"success": True}

@api.delete("/del")
def delete_task(request, task_id:int):
    task_temp = get_object_or_404(Task, id = task_id)
    task_temp.delete()
    return {"success": True}