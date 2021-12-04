def read_file():
    with open('input.txt', 'r') as file:
        lines = [int(line.strip()) for line in file]
    return lines


def part1():
    lines = read_file()
    prev = lines[0]
    inc_count = 0
    for depth in lines:
        if depth > prev:
            inc_count += 1
        prev = depth
    print("increase measurement count: " + str(inc_count))


def part2():
    lines = read_file()
    prev_sum = lines[0] + lines[1] + lines[2]
    inc_count = 0
    for i in range(3, len(lines)):
        new_sum = lines[i] + lines[i-1] + lines[i-2]
        if new_sum > prev_sum:
            inc_count += 1
        prev_sum = new_sum
    print("increase measurement sum count: " + str(inc_count))


if __name__ == '__main__':
    part1()
    part2()
