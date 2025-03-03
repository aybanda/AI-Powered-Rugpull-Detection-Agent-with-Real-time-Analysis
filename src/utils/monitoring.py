from typing import Dict
import time
import uuid
from contextlib import contextmanager
from prometheus_client import Counter, Histogram, start_http_server

class MetricsCollector:
    def __init__(self):
        # Initialize Prometheus metrics
        self.analysis_counter = Counter(
            'token_analysis_total',
            'Total number of token analyses',
            ['status']
        )
        
        self.analysis_latency = Histogram(
            'token_analysis_latency_seconds',
            'Token analysis latency in seconds',
            buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
        )
        
        self.alert_counter = Counter(
            'alerts_generated_total',
            'Total number of alerts generated',
            ['risk_level']
        )
        
        # Start Prometheus metrics server
        start_http_server(8000)
    
    @contextmanager
    def measure_latency(self, operation: str):
        """
        Measure operation latency
        """
        start_time = time.time()
        try:
            yield
        finally:
            duration = time.time() - start_time
            self.analysis_latency.observe(duration)
    
    def increment_counter(self, status: str):
        """
        Increment analysis counter
        """
        self.analysis_counter.labels(status=status).inc()
    
    def record_alert(self, risk_level: str):
        """
        Record generated alert
        """
        self.alert_counter.labels(risk_level=risk_level).inc()
    
    @staticmethod
    def generate_request_id() -> str:
        """
        Generate unique request ID
        """
        return str(uuid.uuid4())
    
    def get_metrics(self) -> Dict:
        """
        Get current metrics
        """
        return {
            'total_analyses': self.analysis_counter._value.sum(),
            'average_latency': self.analysis_latency._sum.sum() / self.analysis_latency._count.sum()
        }