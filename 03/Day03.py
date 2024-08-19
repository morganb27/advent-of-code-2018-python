import fileinput
import re
from collections import defaultdict

PART_1 = 0

PUZZLE = [line.strip() for line in fileinput.input()]
COUNTER = defaultdict(int)

def overlapping_fabric(data):
    global PART_1
    for line in data:
        _, x, y, w, h = parse_input(line)

        for i in range(x, x + w):
            for j in range(y, y + h):
                COUNTER[(i, j)] += 1
    
    for _, value in COUNTER.items():
        if value > 1:
            PART_1 += 1
    print(COUNTER)



def parse_input(line):
    pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    id, x, y, w, h = map(int, re.search(pattern, line).groups())
    return id, x, y, w, h

overlapping_fabric(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")