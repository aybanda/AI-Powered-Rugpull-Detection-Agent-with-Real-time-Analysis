from setuptools import setup, find_packages

setup(
    name="rugpull_detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "web3>=5.31.3",
        "pandas>=1.5.3",
        "numpy>=1.21.0",
        "requests>=2.28.0",
        "torch>=1.13.1",
        "scikit-learn>=1.0.2",
        "fastapi>=0.95.0",
        "uvicorn>=0.21.0",
        "pydantic>=1.10.0",
        "prometheus-client>=0.16.0",
        "python-dotenv>=0.21.0",
        "aiohttp>=3.8.0",
    ],
)