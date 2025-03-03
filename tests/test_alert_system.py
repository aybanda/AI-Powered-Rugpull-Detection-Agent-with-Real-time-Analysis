import pytest
from src.utils.alert_system import AlertSystem, RiskLevel

@pytest.fixture
def alert_system():
    return AlertSystem()

@pytest.fixture
def sample_risk_data():
    return {
        'risk_score': 0.8,
        'explanation': {
            'liquidity_risk': 'High',
            'contract_risk': 'Medium'
        }
    }

async def test_process_alert(alert_system, sample_risk_data):
    token_address = "0x1234567890123456789012345678901234567890"
    await alert_system.process_alert(token_address, sample_risk_data)
    # Assert alert was processed (check logs or mock notifications)

def test_determine_risk_level(alert_system):
    assert alert_system._determine_risk_level(0.2) == RiskLevel.LOW
    assert alert_system._determine_risk_level(0.4) == RiskLevel.MEDIUM
    assert alert_system._determine_risk_level(0.7) == RiskLevel.HIGH
    assert alert_system._determine_risk_level(0.95) == RiskLevel.CRITICAL