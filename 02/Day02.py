import fileinput
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, None


def checksum(data):
    global PART_1
    count_two, count_three = 0, 0
    for line in data:
        c = Counter(line)
        if any(count == 2 for _, count in c.items()):
            count_two += 1
        if any(count == 3 for _, count in c.items()):
            count_three += 1
    PART_1 = count_two * count_three


def box_ids(data):
    global PART_2
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            difference = 0
            for k in range(len(data[i])):
                if data[i][k] != data[j][k]:
                    difference += 1
            if difference == 1:
                PART_2 = ''.join(a for a, b in zip(data[i], data[j]) if a == b)


checksum(PUZZLE)
box_ids(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"SOlution to part 2 is: {PART_2}")