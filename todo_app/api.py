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


@api.get('/filter', response={200: list[schema.TaskOut], 400: schema.Message})
def filter_task(request, filter: str):
    if filter == 'personal':
        task_temp = Task.filters.personal()
    elif filter == 'work':
        task_temp = Task.filters.work()
    elif filter == 'all':
        task_temp = Task.objects.all()
    else:
        return 400, schema.Message(message=f"{filter} is not a valid filter.")
    return task_temp


@api.post('/post', response=schema.TaskOut)
def post_task(request, payload: schema.TaskIn):
    data = payload.dict(exclude_none=True)
    task_temp = Task.objects.create(**data)
    return task_temp


@api.put('/put', response=schema.TaskOut)
def put_task(request, task_id: int, payload: schema.TaskPut):
    task_temp = get_object_or_404(Task, id=task_id)
    data = payload.dict(exclude_unset=True, exclude_none=True)
    for key, value in data.items():
        setattr(task_temp, key, value)
    task_temp.save()
    return task_temp

@api.put('/upd')
def upd_task(request, task_id: int):
    task_temp = get_object_or_404(Task, id=task_id)
    task_temp.is_completed = not task_temp.is_completed
    task_temp.save()
    return {"success": True}

@api.delete("/del")
def del_task(request, task_id: str):
    if task_id == 'all':
        Task.objects.all().delete()
        return {"success": True}
    else:
        task_id = int(task_id)
        task_temp = get_object_or_404(Task, id=task_id)
        task_temp.delete()
        return {"success": True}
