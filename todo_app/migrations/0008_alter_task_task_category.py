# Generated by Django 4.1.7 on 2023-02-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_task_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Work', 'Work')], default='Personal', max_length=8),
        ),
    ]