import torch
import torch.nn as nn

class SmoothTop1SVM(nn.Module):
    def __init__(self, n_classes=None):
        super(SmoothTop1SVM, self).__init__()
        self.n_classes = n_classes

    def forward(self, logits, labels):
        # Convertir les labels en -1 et 1 (binaire)
        labels = 2 * labels.float() - 1
        
        # Extraire le score du logit de la classe prédite pour chaque échantillon
        # Par exemple, pour chaque échantillon, on prend le logit de la classe avec la plus grande valeur
        logits = logits.max(dim=1)[0]  # Cette ligne extrait la classe ayant le score le plus élevé

        # Vérification des dimensions
        print("logits shape:", logits.shape)  # Devrait être (batch_size,)
        print("labels shape:", labels.shape)  # Devrait être (batch_size,)

        # Calcul de la perte
        loss = torch.mean(torch.clamp(1 - labels * logits, min=0) ** 2)
        return loss
