# Generated by Django 4.1.7 on 2023-02-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_task_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(default=models.CharField(max_length=16), max_length=50),
        ),
    ]