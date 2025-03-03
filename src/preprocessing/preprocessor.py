from typing import Dict, List
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataPreprocessor:
    def __init__(self):
        self.required_fields = [
            'contract_data',
            'liquidity_data',
            'transaction_data',
            'social_data'
        ]
    
    def preprocess_token_data(self, raw_data: Dict) -> Dict:
        """
        Preprocess and validate raw token data
        """
        processed_data = {}
        
        # Validate required fields
        self._validate_data(raw_data)
        
        # Process contract data
        processed_data['contract'] = self._process_contract_data(
            raw_data['contract_data']
        )
        
        # Process liquidity data
        processed_data['liquidity'] = self._process_liquidity_data(
            raw_data['liquidity_data']
        )
        
        # Process transaction data
        processed_data['transactions'] = self._process_transaction_data(
            raw_data['transaction_data']
        )
        
        return processed_data
    
    def _validate_data(self, data: Dict) -> None:
        """
        Validate that all required fields are present
        """
        missing_fields = [
            field for field in self.required_fields 
            if field not in data
        ]
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
    
    def _process_contract_data(self, contract_data: Dict) -> Dict:
        """
        Process and standardize contract data
        """
        return {
            'creation_date': self._parse_date(contract_data.get('creation_date')),
            'verified': bool(contract_data.get('verified')),
            'source_code': contract_data.get('source_code', ''),
            'compiler_version': contract_data.get('compiler_version'),
            'has_proxy': self._check_proxy_pattern(contract_data.get('source_code', ''))
        }
    
    def _process_liquidity_data(self, liquidity_data: Dict) -> Dict:
        """
        Process and standardize liquidity data
        """
        return {
            'total_liquidity_usd': float(liquidity_data.get('total_liquidity_usd', 0)),
            'locked_liquidity_usd': float(liquidity_data.get('locked_liquidity_usd', 0)),
            'lock_duration_days': float(liquidity_data.get('lock_duration_days', 0)),
            'pair_addresses': liquidity_data.get('pair_addresses', [])
        }
    
    def _process_transaction_data(self, transaction_data: List[Dict]) -> Dict:
        """
        Process and analyze transaction patterns
        """
        df = pd.DataFrame(transaction_data)
        
        return {
            'daily_volume': self._calculate_daily_volume(df),
            'unique_holders': self._calculate_unique_holders(df),
            'volume_trend': self._calculate_volume_trend(df),
            'large_transactions': self._identify_large_transactions(df)
        }
    
    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """
        Parse date string to datetime object
        """
        try:
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            return None
    
    @staticmethod
    def _check_proxy_pattern(source_code: str) -> bool:
        """
        Check if contract implements proxy pattern
        """
        proxy_indicators = [
            'delegatecall',
            'upgradeability',
            'proxy',
            'implementation'
        ]
        return any(indicator in source_code.lower() for indicator in proxy_indicators)