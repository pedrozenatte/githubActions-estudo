def test_post_tasks_creates_task(client):
    response = client.post("/tasks", json={"title": "Create CI pipeline"})

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Create CI pipeline",
        "done": False,
    }


def test_get_tasks_lists_tasks(client):
    client.post("/tasks", json={"title": "First task"})
    client.post("/tasks", json={"title": "Second task"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "First task", "done": False},
        {"id": 2, "title": "Second task", "done": False},
    ]


def test_get_task_by_id_returns_correct_task(client):
    created = client.post("/tasks", json={"title": "Deploy app"}).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_put_task_updates_task(client):
    created = client.post("/tasks", json={"title": "Draft workflow"}).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={"title": "Review workflow", "done": True},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": created["id"],
        "title": "Review workflow",
        "done": True,
    }


def test_delete_task_removes_task(client):
    created = client.post("/tasks", json={"title": "Remove me"}).json()

    delete_response = client.delete(f"/tasks/{created['id']}")
    get_response = client.get(f"/tasks/{created['id']}")

    assert delete_response.status_code == 204
    assert get_response.status_code == 404


def test_get_missing_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_post_task_with_empty_title_returns_error(client):
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code in (400, 422)
