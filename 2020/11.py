import copy
# -------------------- brute force solution, can be extremely slow -------------------


def read_file():
    with open('11.txt', 'r') as file:
        lines = [list(line.strip()) for line in file]
    return lines


def count_occupied(y, x):
    c = 0
    for a in range(y - 1, y + 2):
        for b in range(x - 1, x + 2):
            if not (a == y and b == x) and 0 <= a < len(data) and 0 <= b < len(data[0]) and data[a][b] == '#':
                c += 1
    return c


def iterate(min_count, count_method):
    new_list = copy.deepcopy(data)
    changed = False
    for m in range(len(data)):
        for n in range(len(data[0])):
            if data[m][n] == 'L' and count_method(m, n) == 0:
                new_list[m][n] = '#'
                changed = True
            elif data[m][n] == '#' and count_method(m, n) >= min_count:
                new_list[m][n] = 'L'
                changed = True
    return new_list, changed


def find(y, x, y_inc, x_inc):
    while 0 <= y+y_inc < len(data) and 0 <= x+x_inc < len(data[0]):
        y += y_inc
        x += x_inc
        if data[y][x] == '#':
            return True
        elif data[y][x] == 'L':
            return False
    return False


def count_occupied2(y, x):
    c = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if (not(a == 0 and b == 0)) and find(y, x, a, b):
                c += 1
    return c


# part 1
data = read_file()
empty, state = iterate(4, count_occupied)
while state:
    data, state = iterate(4, count_occupied)
count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            count += 1
print("part 1 = " + str(count))
# part 2
data = read_file()
empty, state = iterate(5, count_occupied2)
while state:
    data, state = iterate(5, count_occupied2)
count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            count += 1
print("part 2 = " + str(count))
