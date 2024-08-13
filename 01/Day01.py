import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
PART_1, PART_2 = 0, None

def calibration(data):
    global PART_1
    for line in data:
        PART_1 += int(line)

def calibration_part_two(data):
    sum, i = 0, 0
    s = set()
    global PART_2
    while True:
        sum += int(data[i % len(data)])
        if sum not in s:
            s.add(sum)
        else:
            PART_2 = sum
            return
        i += 1







calibration(PUZZLE)
calibration_part_two(PUZZLE)
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")