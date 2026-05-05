from fastapi import FastAPI, HTTPException, Response, status

from app.models import Task, TaskCreate, TaskUpdate
from app.repository import TaskRepository
from app.services import TaskService

app = FastAPI(title="Taskflow API", version="0.1.0")

repository = TaskRepository()
service = TaskService(repository)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return service.list_tasks()


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    try:
        return service.create_task(payload.title)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    return service.get_task(task_id)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    try:
        return service.update_task(task_id, title=payload.title, done=payload.done)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    service.delete_task(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
