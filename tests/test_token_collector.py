import pytest
from src.data_collection.token_collector import TokenDataCollector

@pytest.fixture
def token_collector():
    return TokenDataCollector()

@pytest.fixture
def sample_token_address():
    return "0x1234567890123456789012345678901234567890"

@pytest.mark.asyncio
async def test_get_token_info(token_collector, sample_token_address):
    token_data = await token_collector.get_token_info(sample_token_address)
    
    assert isinstance(token_data, dict)
    assert 'address' in token_data
    assert 'contract_data' in token_data
    assert 'liquidity_data' in token_data
    assert 'transaction_data' in token_data
    assert token_data['address'] == sample_token_address

@pytest.mark.asyncio
async def test_get_contract_data(token_collector, sample_token_address):
    contract_data = await token_collector._get_contract_data(sample_token_address)
    
    assert isinstance(contract_data, dict)
    assert 'creation_date' in contract_data
    assert 'verified' in contract_data
    assert 'source_code' in contract_data

@pytest.mark.asyncio
async def test_get_liquidity_data(token_collector, sample_token_address):
    async with aiohttp.ClientSession() as session:
        liquidity_data = await token_collector._get_liquidity_data(sample_token_address, session)
    
    assert isinstance(liquidity_data, dict)
    assert 'total_liquidity_usd' in liquidity_data
    assert 'locked_liquidity_usd' in liquidity_data
    assert 'lock_duration_days' in liquidity_data

@pytest.mark.asyncio
async def test_get_transaction_data(token_collector, sample_token_address):
    async with aiohttp.ClientSession() as session:
        transaction_data = await token_collector._get_transaction_data(sample_token_address, session)
    
    assert isinstance(transaction_data, list)
    assert len(transaction_data) > 0
    assert 'amount' in transaction_data[0]
    assert 'timestamp' in transaction_data[0]