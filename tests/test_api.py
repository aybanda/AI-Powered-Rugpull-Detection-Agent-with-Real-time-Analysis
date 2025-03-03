import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={
            "address": "0x1234567890123456789012345678901234567890",
            "chain_id": 1
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "risk_score" in data
    assert "risk_factors" in data
    assert isinstance(data["risk_score"], float)
    assert isinstance(data["risk_factors"], dict)

def test_invalid_address():
    response = client.post(
        "/analyze",
        json={
            "address": "invalid_address",
            "chain_id": 1
        }
    )
    
    assert response.status_code == 422  # Validation error