def load_synthetic_dataset():
    """Generates an embedded raw data mock: [Feature1, Feature2], Class Label"""
    return [
        ([1.2, 2.3], "Cluster_A"),
        ([1.5, 1.8], "Cluster_A"),
        ([5.1, 6.2], "Cluster_B"),
        ([5.5, 5.9], "Cluster_B")
    ]
