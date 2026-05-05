from app.models import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def list(self) -> list[Task]:
        return list(self._tasks.values())

    def create(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title, done=False)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def update(
        self,
        task_id: int,
        title: str | None = None,
        done: bool | None = None,
    ) -> Task | None:
        task = self.get(task_id)
        if task is None:
            return None

        updated_task = task.model_copy(
            update={
                "title": title if title is not None else task.title,
                "done": done if done is not None else task.done,
            }
        )
        self._tasks[task_id] = updated_task
        return updated_task

    def delete(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def clear(self) -> None:
        self._tasks.clear()
        self._next_id = 1
