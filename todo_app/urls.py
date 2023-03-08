from django.urls import path

from todo_app.views import *

urlpatterns =[
    path('', app, name='home'),
    path('filter', filter, name='filter'),
    path('view/<int:task_id>/',  view_task, name = 'detail'),
    path('view/<int:task_id>/update',  update_task, name ='update'),
    path('view/<int:task_id>/delete',  delete_task, name ='delete'),
    path('view/<int:task_id>/edit',  edit_task, name ='edit'),
    path('view/<int:task_id>/edit/save',  save_task, name ='save'),      
    path('create/' ,  create_task, name ='create'),
    path('create/submit/' ,  submit_task, name ='submit'),

    
]