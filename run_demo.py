import asyncio
from src.data_collection.token_collector import TokenDataCollector
from src.feature_engineering.advanced_features import AdvancedFeatureExtractor
from src.model.rugpull_detector import RugPullDetector

async def main():
    # Initialize components
    collector = TokenDataCollector()
    feature_extractor = AdvancedFeatureExtractor()
    detector = RugPullDetector()

    # Example token address
    token_address = "0x123..."  # Replace with actual token address

    # Collect data
    token_data = await collector.get_token_info(token_address)
    print(f"Token Data: {token_data}")

    # Extract features
    features = feature_extractor.detect_stealth_marketing(token_data)
    print(f"Features: {features}")

    # Get risk assessment
    risk_score = detector.predict_risk(features)
    print(f"Risk Score: {risk_score}")

if __name__ == "__main__":
    asyncio.run(main())