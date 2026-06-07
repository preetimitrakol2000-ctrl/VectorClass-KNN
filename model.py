from distance import euclidean_distance
from data_loader import load_synthetic_dataset

class CustomKNN:
    def __init__(self, k=3):
        self.k = k
        self.dataset = []

    def fit(self, training_data):
        self.dataset = training_data

    def predict(self, query_point):
        distances = []
        for features, label in self.dataset:
            dist = euclidean_distance(query_point, features)
            distances.append((dist, label))
        
        # Sort values ascending by spatial distance metric
        distances.sort(key=lambda x: x[0])
        neighbors = distances[:self.k]
        
        # Majority voting calculation
        votes = {}
        for _, label in neighbors:
            votes[label] = votes.get(label, 0) + 1
            
        return max(votes, key=votes.get)

if __name__ == "__main__":
    knn = CustomKNN(k=3)
    knn.fit(load_synthetic_dataset())
    
    test_node = [4.8, 5.5]
    prediction = knn.predict(test_node)
    
    print("📈 VectorClass-KNN Processing System Engine...")
    print(f"🎯 Target Input Coordinates: {test_node}")
    print(f"✨ Model Classified Category Result: [{prediction}]")
