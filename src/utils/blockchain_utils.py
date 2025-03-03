from web3 import Web3
from typing import Dict, List
import json

class BlockchainUtils:
    def __init__(self, web3_provider: str):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
    
    def get_contract_abi(self, address: str) -> List:
        """
        Get contract ABI from verified contract
        """
        # Implementation to fetch ABI from Etherscan
        pass
    
    def check_token_balance(self, token_address: str, wallet_address: str) -> float:
        """
        Get token balance for a specific wallet
        """
        try:
            contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(token_address),
                abi=self.get_contract_abi(token_address)
            )
            balance = contract.functions.balanceOf(
                Web3.to_checksum_address(wallet_address)
            ).call()
            decimals = contract.functions.decimals().call()
            return balance / (10 ** decimals)
        except Exception as e:
            print(f"Error checking balance: {e}")
            return 0.0
    
    def analyze_contract_security(self, address: str, source_code: str) -> Dict:
        """
        Analyze contract for common security issues
        """
        security_issues = []
        
        # Check for common vulnerabilities
        if 'selfdestruct' in source_code:
            security_issues.append('Contains selfdestruct function')
        
        if 'transfer(' in source_code and 'safeTransfer(' not in source_code:
            security_issues.append('Uses unsafe transfer method')
        
        if 'tx.origin' in source_code:
            security_issues.append('Uses tx.origin')
        
        return {
            'has_security_issues': len(security_issues) > 0,
            'issues': security_issues
        }