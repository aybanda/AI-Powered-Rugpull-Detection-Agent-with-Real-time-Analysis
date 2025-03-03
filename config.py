from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# API Configuration
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"
WEB3_PROVIDER_URL = "YOUR_WEB3_PROVIDER_URL"
DEXSCREENER_API_URL = "https://api.dexscreener.com/latest"

# Model Configuration
MODEL_PARAMS = {
    "input_dim": 6,
    "hidden_dim": 64,
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100
}

# Feature Engineering Parameters
LIQUIDITY_THRESHOLD = 1000  # Minimum liquidity in USD
TRANSACTION_HISTORY_DAYS = 7  # Days of transaction history to analyze
HOLDER_CONCENTRATION_THRESHOLD = 0.5  # Maximum acceptable concentration