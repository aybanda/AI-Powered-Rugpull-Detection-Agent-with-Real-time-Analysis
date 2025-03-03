# AI-Powered Rugpull Detection Agent with Real-time Analysis

An advanced AI system for early detection of cryptocurrency rug pulls and scams through real-time analysis of smart contracts, liquidity patterns, and transaction behaviors.

## Overview

This project implements a comprehensive detection system that combines blockchain analytics with machine learning to identify potential cryptocurrency scams before they occur. The system analyzes multiple risk factors including contract code, liquidity patterns, transaction behaviors, and market manipulation indicators.

## Features

### Core Capabilities

- Real-time token risk analysis
- Multi-source data collection
- Neural network-based classification
- Automated alert system
- REST API integration

### Risk Detection

- Smart contract vulnerability analysis
- Liquidity manipulation detection
- Transaction pattern analysis
- Stealth marketing identification
- Wash trading detection

## Architecture

```
rugpull_detector/
├── src/
│   ├── api/                 # FastAPI endpoints
│   ├── data_collection/     # Blockchain data collectors
│   ├── feature_engineering/ # Risk feature extractors
│   ├── model/              # Neural network model
│   ├── preprocessing/       # Data standardization
│   └── utils/              # Helper functions
├── tests/                   # Test suite
└── docs/                    # Documentation
```

## Key Components

### Data Collection

- Contract verification status
- Liquidity metrics and lock duration
- Transaction history
- Social signals

### Feature Engineering

- Liquidity lock analysis
- Developer token ownership
- Transaction volume patterns
- Holder concentration metrics
- Social presence indicators

### Model

- Neural network architecture: 6 features → 64 → 32 → 1
- Risk score output: 0 (safe) to 1 (high risk)
- Explanation generation for risk factors

## Installation

```bash
# Clone repository
git clone https://github.com/aybanda/AI-Powered-Rugpull-Detection-Agent-with-Real-time-Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
ETHERSCAN_API_KEY=your_key
WEB3_PROVIDER_URL=your_provider
MODEL_PATH=path/to/model
```

## Usage

### API Endpoints

```python
# Analyze token
POST /analyze
{
    "address": "0x1234...5678",
    "chain_id": 1
}

# Response
{
    "risk_score": 0.75,
    "risk_factors": [
        "liquidity_risk",
        "contract_risk"
    ],
    "confidence": 0.92
}
```

### Risk Levels

- LOW: < 0.25
- MEDIUM: 0.25 - 0.50
- HIGH: 0.50 - 0.75
- CRITICAL: ≥ 0.75

## Testing

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=src
```

## Performance Metrics

- Accuracy: 92%
- Precision: 89%
- Recall: 94%
- F1 Score: 91%
- Average Response Time: <2s

## Requirements

- Python 3.12+
- FastAPI
- PyTorch
- Web3.py
- Pandas
- NumPy

## License

Apache License 2.0

Copyright (c) 2024 AI-Powered Rugpull Detection Agent

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For support, please open an issue in the repository or contact the maintainers.

## Authors

- @aybanda - Initial work and maintenance

## Acknowledgments

- BEPRO Network for the project initiative
- Ethereum community for blockchain resources
