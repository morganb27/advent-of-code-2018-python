import fileinput
from string import ascii_lowercase, ascii_uppercase

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, float("inf")

def polymer_units(data):
    global PART_1
    for line in data:
        while True:
            curr = len(line)
            for x, X in zip(ascii_lowercase, ascii_uppercase):
                line = line.replace(x + X, '').replace(X + x, '')
            if len(line) == curr:
                PART_1 = len(line)
                return

def polymer_units_part_two(data):
    global PART_2
    for line in data:
        initial_line = line
        for x, X in zip(ascii_lowercase, ascii_uppercase):
            line = initial_line.replace(x, '').replace(X, '')
            while True:
                curr = len(line)
                for x, X in zip(ascii_lowercase, ascii_uppercase):
                    line = line.replace(x + X, '').replace(X + x, '')
                if len(line) == curr:
                    break
            PART_2 = min(PART_2, len(line))              
            


polymer_units(PUZZLE)
polymer_units_part_two(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")