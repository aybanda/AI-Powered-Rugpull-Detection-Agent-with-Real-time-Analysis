import pytest
from src.feature_engineering.advanced_features import AdvancedFeatureExtractor

@pytest.fixture
def feature_extractor():
    return AdvancedFeatureExtractor()

def test_stealth_marketing_detection(feature_extractor):
    token_data = {"address": "0x123..."}
    risk_score = feature_extractor.detect_stealth_marketing(token_data)
    assert 0 <= risk_score <= 1

def test_liquidity_scheme_analysis(feature_extractor):
    token_data = {"address": "0x123..."}
    risk_score = feature_extractor.analyze_liquidity_schemes(token_data)
    assert 0 <= risk_score <= 1
