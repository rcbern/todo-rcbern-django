from pydantic import Field, validator
from ninja import Schema
from datetime import datetime


class Message(Schema):
    message: str


class TaskIn(Schema):
    task_name: str = Field(..., description="Task Name")
    task_description: str = Field(description="Task Description")
    task_category: str = Field(description="Task Category")
    is_completed: bool | None = Field(None, description="Task Status")
    date_completion: datetime | None = Field(None, description="Task Completion")
    date_creation: datetime | None = Field(None, description="Task Creation")

    @validator('task_description')
    def validate_desc(cls, value):
        if len(value) > 50:
            raise ValueError(f"Task description should be less than 50 characters.")
        return value

class TaskPut(Schema):
    task_name: str | None = Field(None, description="Task Name")
    task_description: str | None = Field(None, description="Task Description")
    task_category: str | None = Field(None, description="Task Category")
    is_completed: bool | None = Field(None, description="Task Status")
    date_completion: datetime | None = Field(None, description="Task Completion")
    date_creation: datetime | None = Field(None, description="Task Creation")

    @validator('task_description')
    def validate_desc(cls, value):
        if len(value) > 50:
            raise ValueError(f"Task description should be less than 50 characters.")
        return value


class TaskOut(Schema):
    id: int
    task_name: str | None = Field(None, description="Task Name")
    task_description: str | None = Field(None, description="Task Description")
    # task_category: str | None = Field(None, description="Task Category")
    is_completed: bool | None = Field(None, description="Task Status")
    # date_completion: datetime | None = Field(None, description="Task Completion")
    # date_creation: datetime | None = Field(None, description="Task Creation")
