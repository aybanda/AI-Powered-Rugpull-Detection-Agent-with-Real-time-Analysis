from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime

from ..data_collection.token_collector import TokenDataCollector

app = FastAPI(title="Rugpull Detector API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
collector = TokenDataCollector()

class TokenRequest(BaseModel):
    address: str = Field(
        pattern="^0x[a-fA-F0-9]{40}$",
        description="Ethereum address in hex format"
    )
    chain_id: int = Field(default=1, description="Chain ID (1 for Ethereum mainnet)")

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.now()}

@app.post("/analyze")
async def analyze_token(request: TokenRequest):
    """
    Analyze a token for potential rug pull risks
    """
    try:
        token_data = await collector.get_token_info(request.address)
        return {
            "risk_score": 0.5,
            "risk_factors": {
                "liquidity": "medium",
                "contract": "verified",
                "social": "active"
            },
            "token_data": token_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))