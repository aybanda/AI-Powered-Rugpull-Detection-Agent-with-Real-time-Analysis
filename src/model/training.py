import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from typing import Tuple, List
import numpy as np
from sklearn.model_selection import train_test_split
from ..model.rugpull_detector import RugPullDetector

class TokenDataset(Dataset):
    def __init__(self, features: np.ndarray, labels: np.ndarray):
        self.features = torch.FloatTensor(features)
        self.labels = torch.FloatTensor(labels)
    
    def __len__(self) -> int:
        return len(self.features)
    
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.features[idx], self.labels[idx]

class ModelTrainer:
    def __init__(self, config: dict):
        self.config = config
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = RugPullDetector(
            input_dim=config['input_dim'],
            hidden_dim=config['hidden_dim']
        ).to(self.device)
        
        self.criterion = nn.BCELoss()
        self.optimizer = torch.optim.Adam(
            self.model.parameters(),
            lr=config['learning_rate']
        )
    
    def train(self, features: np.ndarray, labels: np.ndarray) -> Dict:
        """
        Train the model with given features and labels
        """
        # Split data
        X_train, X_val, y_train, y_val = train_test_split(
            features, labels, test_size=0.2, random_state=42
        )
        
        # Create data loaders
        train_dataset = TokenDataset(X_train, y_train)
        val_dataset = TokenDataset(X_val, y_val)
        
        train_loader = DataLoader(
            train_dataset,
            batch_size=self.config['batch_size'],
            shuffle=True
        )
        val_loader = DataLoader(
            val_dataset,
            batch_size=self.config['batch_size']
        )
        
        # Training loop
        best_val_loss = float('inf')
        training_history = []
        
        for epoch in range(self.config['epochs']):
            train_loss = self._train_epoch(train_loader)
            val_loss = self._validate(val_loader)
            
            training_history.append({
                'epoch': epoch,
                'train_loss': train_loss,
                'val_loss': val_loss
            })
            
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                self._save_model()
            
            print(f"Epoch {epoch}: Train Loss = {train_loss:.4f}, Val Loss = {val_loss:.4f}")
        
        return {'training_history': training_history, 'best_val_loss': best_val_loss}
    
    def _train_epoch(self, train_loader: DataLoader) -> float:
        """
        Train for one epoch
        """
        self.model.train()
        total_loss = 0
        
        for features, labels in train_loader:
            features, labels = features.to(self.device), labels.to(self.device)
            
            self.optimizer.zero_grad()
            outputs = self.model(features)
            loss = self.criterion(outputs, labels)
            
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(train_loader)
    
    def _validate(self, val_loader: DataLoader) -> float:
        """
        Validate the model
        """
        self.model.eval()
        total_loss = 0
        
        with torch.no_grad():
            for features, labels in val_loader:
                features, labels = features.to(self.device), labels.to(self.device)
                outputs = self.model(features)
                loss = self.criterion(outputs, labels)
                total_loss += loss.item()
        
        return total_loss / len(val_loader)
    
    def _save_model(self) -> None:
        """
        Save the model weights
        """
        torch.save(
            self.model.state_dict(),
            'model_weights.pth'
        )