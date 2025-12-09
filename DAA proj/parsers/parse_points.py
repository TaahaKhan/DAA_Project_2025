# parsers/parse_points.py

def parse_points_file(path):
    points = []

    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            x, y = map(int, line.split())
            points.append((x, y))

    return sorted(points, key=lambda p: p[0])
