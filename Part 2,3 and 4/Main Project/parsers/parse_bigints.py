# parsers/parse_bigints.py

def parse_bigint_file(path):
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    return lines[0], lines[1]
