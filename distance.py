import math

def euclidean_distance(point1, point2):
    """Calculates multidimensional space straight-line distance variance."""
    squared_sum = 0.0
    for i in range(len(point1)):
        squared_sum += (point1[i] - point2[i]) ** 2
    return math.sqrt(squared_sum)
