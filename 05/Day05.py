import fileinput
from string import ascii_lowercase, ascii_uppercase

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1 = 0

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
                
            


polymer_units(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")