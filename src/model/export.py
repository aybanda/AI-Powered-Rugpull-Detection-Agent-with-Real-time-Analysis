from typing import Literal
import torch
import tensorflow as tf
from .rugpull_detector import RugPullDetector

def export_model(
    model: RugPullDetector,
    format: Literal["pytorch", "tensorflow"] = "pytorch",
    path: str = "models"
) -> str:
    """
    Export the model in the specified format
    """
    if format == "pytorch":
        # Export PyTorch model
        torch.save(model.state_dict(), f"{path}/model.pt")
        return f"{path}/model.pt"
    else:
        # Export TensorFlow model
        # ... implementation ...
        return f"{path}/model.tf"