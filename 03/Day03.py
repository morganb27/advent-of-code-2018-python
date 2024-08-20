import fileinput
import re
from collections import defaultdict

PART_1 = 0
PART_2 = None

PUZZLE = [line.strip() for line in fileinput.input()]
COUNTER = defaultdict(int)
CLAIMS = defaultdict(list)

def overlapping_fabric(data):
    global PART_1, CLAIMS, PART_2
    for line in data:
        id, x, y, w, h = parse_input(line)

        for i in range(x, x + w):
            for j in range(y, y + h):
                COUNTER[(i, j)] += 1
                CLAIMS[id].append((i, j))
    
    for _, value in COUNTER.items():
        if value > 1:
            PART_1 += 1

    for id, coordinates in CLAIMS.items():
        for pos in coordinates:
            if COUNTER[pos] > 1:
                break
        else:
            PART_2 = id




def parse_input(line):
    pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    id, x, y, w, h = map(int, re.search(pattern, line).groups())
    return id, x, y, w, h

overlapping_fabric(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")