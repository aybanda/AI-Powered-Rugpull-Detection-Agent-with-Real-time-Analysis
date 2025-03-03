import torch
import torch.nn as nn
from typing import Dict, Tuple

class RugPullDetector(nn.Module):
    def __init__(self, input_dim: int = 6, hidden_dim: int = 64):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim // 2, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)
    
    def predict_risk(self, features: torch.Tensor) -> Tuple[float, Dict]:
        """
        Predict rug pull risk and provide explanation
        """
        with torch.no_grad():
            risk_score = self.forward(features).item()
            
        explanation = self._generate_risk_explanation(features, risk_score)
        return risk_score, explanation
    
    def _generate_risk_explanation(self, features: torch.Tensor, risk_score: float) -> Dict:
        """
        Generate human-readable explanation for the risk score
        """
        return {
            'risk_level': self._get_risk_level(risk_score),
            'contributing_factors': {
                'liquidity': 'high' if features[0][0].item() > 0.5 else 'low',
                'developer_tokens': 'high' if features[0][1].item() > 0.5 else 'low',
                'social_presence': 'high' if features[0][2].item() > 0.5 else 'low',
                'transaction_pattern': 'suspicious' if features[0][3].item() > 0.5 else 'normal',
                'holder_distribution': 'concentrated' if features[0][4].item() > 0.5 else 'distributed',
                'contract_risk': 'high' if features[0][5].item() > 0.5 else 'low'
            }
        }
    
    @staticmethod
    def _get_risk_level(risk_score: float) -> str:
        if risk_score < 0.3:
            return 'LOW'
        elif risk_score < 0.6:
            return 'MEDIUM'
        elif risk_score < 0.8:
            return 'HIGH'
        else:
            return 'CRITICAL'