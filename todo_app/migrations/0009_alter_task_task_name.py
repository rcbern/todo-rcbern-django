# Generated by Django 4.1.7 on 2023-02-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_alter_task_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=32),
        ),
    ]
