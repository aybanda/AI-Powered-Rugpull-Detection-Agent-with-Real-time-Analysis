import pytest
import torch
from src.model.rugpull_detector import RugPullDetector

@pytest.fixture
def model():
    return RugPullDetector(input_dim=6, hidden_dim=64)

@pytest.fixture
def sample_features():
    return torch.rand(1, 6)

def test_model_initialization(model):
    assert isinstance(model, RugPullDetector)
    assert next(model.parameters()).requires_grad

def test_model_forward(model, sample_features):
    output = model(sample_features)
    
    assert isinstance(output, torch.Tensor)
    assert output.shape == (1, 1)
    assert 0 <= output.item() <= 1

def test_predict_risk(model, sample_features):
    risk_score, explanation = model.predict_risk(sample_features)
    
    assert isinstance(risk_score, float)
    assert isinstance(explanation, dict)
    assert 0 <= risk_score <= 1