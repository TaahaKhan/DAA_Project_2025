import random
import math
import os

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points)//2
    mid_point = points[mid]
    left = points[:mid]
    right = points[mid:]

    d_left = closest_pair(left)
    d_right = closest_pair(right)
    d = min(d_left, d_right)

    strip = [p for p in points if abs(p[0]-mid_point[0]) < d]
    return min(d, strip_closest(strip, d))

os.makedirs("closest_inputs", exist_ok=True)

for i in range(1, 11):
    points = [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(100 + i*10)]
    with open(f"closest_inputs/points_{i}.txt", "w") as f:
        for x, y in points:
            f.write(f"{x} {y}\n")

print("✅ Generated 10 input files for Closest Pair in folder: closest_inputs/")

os.makedirs("closest_results", exist_ok=True)

for i in range(1, 11):
    with open(f"closest_inputs/points_{i}.txt") as f:
        points = [tuple(map(int, line.split())) for line in f.readlines()]
        points.sort(key=lambda p: p[0])
        min_dist = closest_pair(points)
        print(f"Dataset {i} → Closest Distance: {min_dist:.4f}")
        with open(f"closest_results/result_{i}.txt", "w") as out:
            out.write(f"Closest Pair Distance for dataset {i}: {min_dist:.4f}\n")

print("✅ Results saved in: closest_results/")
