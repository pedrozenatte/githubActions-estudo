from fastapi import HTTPException, status

from app.models import Task
from app.repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def list_tasks(self) -> list[Task]:
        return self.repository.list()

    def create_task(self, title: str) -> Task:
        normalized_title = title.strip()
        if not normalized_title:
            raise ValueError("Task title cannot be empty")

        return self.repository.create(normalized_title)

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get(task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )
        return task

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        done: bool | None = None,
    ) -> Task:
        normalized_title = title.strip() if title is not None else None
        if title is not None and not normalized_title:
            raise ValueError("Task title cannot be empty")

        task = self.repository.update(task_id, title=normalized_title, done=done)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )
        return task

    def delete_task(self, task_id: int) -> None:
        deleted = self.repository.delete(task_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )
