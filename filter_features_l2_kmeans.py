import os
import torch
import numpy as np
from sklearn.cluster import KMeans
from tqdm import tqdm
import argparse

def filter_l2_kmeans(pt_dir, save_dir, keep_ratio=0.3, n_clusters=10, keep_top_clusters=1):
    os.makedirs(save_dir, exist_ok=True)
    pt_files = [f for f in os.listdir(pt_dir) if f.endswith('.pt')]

    for pt_file in tqdm(pt_files, desc="Filtrage L2 + KMeans"):
        path = os.path.join(pt_dir, pt_file)
        features = torch.load(path)  # shape: [N, D]
        features_np = features.numpy()

        # Étape 1 : filtrage L2
        l2_norms = np.linalg.norm(features_np, axis=1)
        keep_count = int(len(features_np) * keep_ratio)
        if keep_count < n_clusters:
            torch.save(features, os.path.join(save_dir, pt_file))
            continue
        top_indices = np.argsort(l2_norms)[-keep_count:]
        filtered_l2 = features_np[top_indices]

        # Étape 2 : KMeans sur vecteurs filtrés
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(filtered_l2)
        dominant_clusters = np.argsort(np.bincount(labels))[-keep_top_clusters:]
        keep_mask = np.isin(labels, dominant_clusters)
        final_filtered = filtered_l2[keep_mask]

        # Sauvegarde
        if len(final_filtered) == 0:
            continue
        torch.save(torch.tensor(final_filtered), os.path.join(save_dir, pt_file))

    print(f"✅ Filtrage terminé : L2 + KMeans. Résultats dans {save_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pt_dir', type=str, required=True)
    parser.add_argument('--save_dir', type=str, required=True)
    parser.add_argument('--keep_ratio', type=float, default=0.3)
    parser.add_argument('--n_clusters', type=int, default=10)
    parser.add_argument('--keep_top_clusters', type=int, default=1)
    args = parser.parse_args()

    filter_l2_kmeans(
        pt_dir=args.pt_dir,
        save_dir=args.save_dir,
        keep_ratio=args.keep_ratio,
        n_clusters=args.n_clusters,
        keep_top_clusters=args.keep_top_clusters
    )
