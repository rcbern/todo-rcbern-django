from django.db import models
from django.utils import timezone


class TaskQuerySet(models.QuerySet):
    def personal(self):
        return self.filter(task_category__exact='personal')

    def work(self):
        return self.filter(task_category__exact='work')

    def is_completed(self):
        return self.filter(is_completed=True)

    def to_complete(self):
        return self.filter(is_completed=False)


class Task(models.Model):
    class TaskCategory(models.TextChoices):
        PERSONAL = 'personal'
        WORK = 'work'

    task_name = models.CharField(max_length=32)
    task_description = models.TextField(max_length=50, null=True, blank=True)
    task_category = models.CharField(max_length=8, choices=TaskCategory.choices,
                                     default=TaskCategory.PERSONAL)
    is_completed = models.BooleanField(default=False)
    date_completion = models.DateTimeField(default=timezone.now)
    date_creation = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    filters = TaskQuerySet.as_manager()

    def __str__(self):
        return self.task_name

# Create your models here.
