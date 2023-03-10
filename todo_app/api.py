from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from todo_app.models import Task
import todo_app.schema as schema

api = NinjaAPI()


@api.get('/all', response=list[schema.TaskOut])
def all_task(request):
    task_temp = Task.objects.all()
    return task_temp


@api.get('/get', response=schema.TaskOut)
def get_task(request, task_id: int):
    task_temp = get_object_or_404(Task, id=task_id)
    return task_temp


@api.get('/filter', response={200: list[schema.TaskOut], 500: schema.Message})
def filter_task(request, filter: str):
    if filter == 'Personal':
        task_temp = Task.filters.personal()
    elif filter == 'Work':
        task_temp = Task.filters.work()
    else:
        return 500, schema.Message(message=f"{filter} is not a valid filter.")
    return 200, task_temp


@api.post('/post', response=schema.TaskOut)
def post_task(request, payload: schema.TaskIn):
    data = payload.dict(exclude_none=True)
    task_temp = Task.objects.create(**data)
    return task_temp


@api.put('/put', response=schema.TaskOut)
def update_task(request, task_id: int, payload: schema.TaskPut):
    task_temp = get_object_or_404(Task, id=task_id)
    data = payload.dict(exclude_unset=True, exclude_none=True)
    for key, value in data.items():
        setattr(task_temp, key, value)
    task_temp.save()
    return task_temp


@api.delete("/del")
def delete_task(request, task_id: str):
    if task_id == 'all':
        Task.objects.all().delete()
        return {"success": True}
    else:
        task_id = int(task_id)
        task_temp = get_object_or_404(Task, id=task_id)
        task_temp.delete()
        return {"success": True}
