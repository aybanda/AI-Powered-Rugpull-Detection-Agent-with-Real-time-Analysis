from typing import Dict, List
import numpy as np
from datetime import datetime

class FeatureExtractor:
    def __init__(self):
        self.feature_names = [
            'liquidity_lock_duration',
            'dev_token_percentage',
            'social_score',
            'transaction_volume_volatility',
            'holder_concentration',
            'contract_risk_score'
        ]
    
    def extract_features(self, token_data: Dict) -> np.ndarray:
        """
        Extract relevant features from token data
        """
        features = []
        
        # Liquidity features
        features.append(self._calculate_liquidity_lock_duration(token_data))
        features.append(self._calculate_dev_token_percentage(token_data))
        
        # Social features
        features.append(self._calculate_social_score(token_data))
        
        # Transaction features
        features.append(self._calculate_volume_volatility(token_data))
        features.append(self._calculate_holder_concentration(token_data))
        
        # Contract features
        features.append(self._analyze_contract_risk(token_data))
        
        return np.array(features)
    
    def _calculate_liquidity_lock_duration(self, token_data: Dict) -> float:
        """
        Calculate the duration of liquidity lock
        """
        liquidity_data = token_data.get('liquidity_data', {})
        lock_duration = liquidity_data.get('lock_duration_days', 0)
        return float(lock_duration)
    
    def _calculate_dev_token_percentage(self, token_data: Dict) -> float:
        """
        Calculate percentage of tokens held by developers
        """
        return 0.1  # Mock implementation
    
    def _calculate_social_score(self, token_data: Dict) -> float:
        """
        Calculate social presence score
        """
        return 0.5  # Mock implementation
    
    def _calculate_volume_volatility(self, token_data: Dict) -> float:
        """
        Calculate transaction volume volatility
        """
        return 0.3  # Mock implementation
    
    def _calculate_holder_concentration(self, token_data: Dict) -> float:
        """
        Calculate token holder concentration
        """
        return 0.4  # Mock implementation
    
    def _analyze_contract_risk(self, token_data: Dict) -> float:
        """
        Analyze contract for risk factors
        """
        return 0.2  # Mock implementation