from fastapi.testclient import TestClient
from main import app
import main

# TestClient crea un server virtuale istantaneo per eseguire i test
client = TestClient(app)

def test_health_check_up():
    """Verifica che il server risponda 200 OK quando è in salute"""
    main.HEALTHY = True
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP", "message": "Servizio Attivo"}

def test_health_check_down():
    """Verifica che il server risponda 503 se si verifica un guasto"""
    main.HEALTHY = False
    response = client.get("/health")
    assert response.status_code == 503
    assert response.json() == {"status": "DOWN", "message": "Service Unavailable"}
