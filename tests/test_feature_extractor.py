import pytest
import numpy as np
from src.feature_engineering.feature_extractor import FeatureExtractor

@pytest.fixture
def feature_extractor():
    return FeatureExtractor()

@pytest.fixture
def sample_token_data():
    return {
        'liquidity_data': {
            'total_liquidity_usd': 100000,
            'locked_liquidity_usd': 50000,
            'lock_duration_days': 365
        },
        'transaction_data': [
            {'amount': 1000, 'timestamp': '2023-01-01T00:00:00'},
            {'amount': 2000, 'timestamp': '2023-01-02T00:00:00'}
        ],
        'contract_data': {
            'creation_date': '2023-01-01T00:00:00',
            'verified': True,
            'source_code': 'contract Token {...}'
        },
        'social_data': {
            'telegram_members': 1000,
            'twitter_followers': 5000,
            'github_commits': 50
        }
    }

def test_extract_features(feature_extractor, sample_token_data):
    features = feature_extractor.extract_features(sample_token_data)
    
    assert isinstance(features, np.ndarray)
    assert len(features) == len(feature_extractor.feature_names)
    assert all(isinstance(x, (int, float)) for x in features)

def test_calculate_liquidity_lock_duration(feature_extractor, sample_token_data):
    duration = feature_extractor._calculate_liquidity_lock_duration(sample_token_data)
    assert isinstance(duration, float)
    assert duration == 365.0