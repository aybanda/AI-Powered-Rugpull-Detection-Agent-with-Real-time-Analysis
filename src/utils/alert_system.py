from typing import Dict, List
import asyncio
import logging
from datetime import datetime
from enum import Enum

class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class AlertSystem:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.risk_thresholds = {
            RiskLevel.LOW: 0.25,
            RiskLevel.MEDIUM: 0.5,
            RiskLevel.HIGH: 0.75,
            RiskLevel.CRITICAL: 0.9
        }
    
    async def process_alert(self, token_address: str, risk_data: Dict) -> None:
        """
        Process and distribute alerts based on risk level
        """
        risk_score = risk_data['risk_score']
        risk_level = self._determine_risk_level(risk_score)
        
        alert = self._create_alert(token_address, risk_data, risk_level)
        await self._distribute_alert(alert)
        
    def _determine_risk_level(self, risk_score: float) -> RiskLevel:
        """
        Determine risk level based on risk score
        """
        for level, threshold in self.risk_thresholds.items():
            if risk_score <= threshold:
                return level
        return RiskLevel.CRITICAL
    
    def _create_alert(self, token_address: str, risk_data: Dict, risk_level: RiskLevel) -> Dict:
        """
        Create formatted alert message
        """
        return {
            'timestamp': datetime.now().isoformat(),
            'token_address': token_address,
            'risk_level': risk_level.value,
            'risk_score': risk_data['risk_score'],
            'explanation': risk_data['explanation'],
            'immediate_concerns': self._get_immediate_concerns(risk_data)
        }
    
    async def _distribute_alert(self, alert: Dict) -> None:
        """
        Distribute alert through various channels
        """
        # Log alert
        self.logger.warning(f"High risk token detected: {alert}")
        
        # Implement different distribution methods based on risk level
        if alert['risk_level'] in [RiskLevel.HIGH.value, RiskLevel.CRITICAL.value]:
            await self._send_urgent_notification(alert)
    
    def _get_immediate_concerns(self, risk_data: Dict) -> List[str]:
        """
        Extract immediate concerns from risk data
        """
        concerns = []
        if risk_data.get('liquidity_data', {}).get('locked_liquidity_usd', 0) < 1000:
            concerns.append("Low liquidity lock")
        
        if risk_data.get('holder_concentration', 0) > 0.5:
            concerns.append("High token concentration")
            
        return concerns
    
    async def _send_urgent_notification(self, alert: Dict) -> None:
        """
        Send urgent notifications for high-risk alerts
        """
        # Implement notification logic (e.g., webhook, email, etc.)
        pass