def test_home_endpoint_returns_success(client):
    
    response = client.get("/")

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    
def test_healthcheck_endpoint_returns_healthy(client):
    response = client.get("/api/v1/health")
    data = response.get_json()
    
    assert response.status_code == 200
    assert data["status"] == "healthy"
