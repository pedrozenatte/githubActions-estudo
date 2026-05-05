def test_health_returns_status_200(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_health_response_contains_status_message(client):
    response = client.get("/health")

    assert response.json() == {"status": "ok"}
