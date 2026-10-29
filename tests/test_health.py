from django.test import Client


def test_health_endpoint():

    client = Client()

    response = client.get("/api/v1/health/")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"
