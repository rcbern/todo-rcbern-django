# Generated by Django 4.1.7 on 2023-02-26 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0013_alter_task_date_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
