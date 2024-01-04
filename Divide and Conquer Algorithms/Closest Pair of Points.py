import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest_pair(points):
    n = len(points)
    min_distance = float('inf')
    closest_pair = None
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    return min_distance, closest_pair

def closest_pair_divide_and_conquer(points):
    points = sorted(points, key=lambda x: x[0])
    return divide_and_conquer(points)

def divide_and_conquer(points):
    n = len(points)
    
    if n <= 3:
        return brute_force_closest_pair(points)
    
    mid = n // 2
    left_closest = divide_and_conquer(points[:mid])
    right_closest = divide_and_conquer(points[mid:])
    
    min_distance, closest_pair = min(left_closest, right_closest, key=lambda x: x[0])
    
    strip = [point for point in points if abs(point[0] - points[mid][0]) < min_distance]
    strip_closest = closest_pair_strip(strip, min_distance)
    
    return min(min_distance, strip_closest[0]), strip_closest[1]

def closest_pair_strip(strip, min_distance):
    strip = sorted(strip, key=lambda x: x[1])
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < min_distance:
            min_distance = min(min_distance, euclidean_distance(strip[i], strip[j]))
            j += 1
    
    return min_distance, None

points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
result = closest_pair_divide_and_conquer(points)
print("Jarak terdekat:", result[0])
print("Pasangan titik terdekat:", result[1])