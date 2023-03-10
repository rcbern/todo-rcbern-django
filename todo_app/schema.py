from pydantic import Field
from ninja import Schema
from datetime import date


class TaskIn(Schema):
    task_name: str = Field(..., description="Task Name")
    task_description: str | None = Field(None, description="Task Description")
    task_category: str | None = Field(None, description="Task Category")
    is_completed: bool | None = Field(None, description="Task Status")
    date_completion: date | None = Field(None, description="Task Completion")
    date_creation: date | None = Field(None, description="Task Creation")


class TaskPut(Schema):
    task_name: str | None = Field(None, description="Task Name")
    task_description: str | None = Field(None, description="Task Description")
    task_category: str | None = Field(None, description="Task Category")
    is_completed: bool | None = Field(None, description="Task Status")
    date_completion: date | None = Field(None, description="Task Completion")
    date_creation: date | None = Field(None, description="Task Creation")


class TaskOut(Schema):
    id: int
    task_name: str | None = Field(None, description="Task Name")
    task_description: str | None = Field(None, description="Task Description")
    task_category: str | None = Field(None, description="Task Category")
    # is_completed: bool | None = Field(None, description="Task Status")
    # date_completion: date | None = Field(None, description="Task Completion")
    # date_creation: date | None = Field(None, description="Task Creation")


class Message(Schema):
    message: str