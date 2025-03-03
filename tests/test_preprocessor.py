import pytest
from src.preprocessing.preprocessor import DataPreprocessor

@pytest.fixture
def preprocessor():
    return DataPreprocessor()

def test_data_validation(preprocessor):
    invalid_data = {'contract_data': {}}
    with pytest.raises(ValueError):
        preprocessor._validate_data(invalid_data)

def test_contract_data_processing(preprocessor):
    contract_data = {
        'creation_date': '2023-01-01T00:00:00',
        'verified': True,
        'source_code': 'contract Token {...}',
        'compiler_version': '0.8.0'
    }
    processed = preprocessor._process_contract_data(contract_data)
    assert 'creation_date' in processed
    assert 'verified' in processed
    assert isinstance(processed['verified'], bool)