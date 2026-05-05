import pytest
from fastapi import HTTPException

from app.repository import TaskRepository
from app.services import TaskService


@pytest.fixture
def service() -> TaskService:
    return TaskService(TaskRepository())


def test_create_task(service):
    task = service.create_task("Study GitHub Actions")

    assert task.id == 1
    assert task.title == "Study GitHub Actions"
    assert task.done is False


def test_list_tasks(service):
    service.create_task("First task")
    service.create_task("Second task")

    tasks = service.list_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "First task"
    assert tasks[1].title == "Second task"


def test_get_task_by_id(service):
    created_task = service.create_task("Read docs")

    task = service.get_task(created_task.id)

    assert task == created_task


def test_update_task(service):
    created_task = service.create_task("Old title")

    updated_task = service.update_task(created_task.id, title="New title", done=True)

    assert updated_task.id == created_task.id
    assert updated_task.title == "New title"
    assert updated_task.done is True


def test_delete_task(service):
    created_task = service.create_task("Temporary task")

    service.delete_task(created_task.id)

    with pytest.raises(HTTPException) as exc_info:
        service.get_task(created_task.id)

    assert exc_info.value.status_code == 404


def test_get_missing_task_raises_404(service):
    with pytest.raises(HTTPException) as exc_info:
        service.get_task(999)

    assert exc_info.value.status_code == 404


def test_create_task_with_empty_title_raises_error(service):
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.create_task("   ")
