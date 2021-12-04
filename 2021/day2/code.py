def read_file():
    with open('input.txt', 'r') as file:
        lines = [line.strip().split(" ") for line in file]
    return lines


def part1():
    instr = read_file()
    hor = 0
    ver = 0
    for step in instr:
        x = int(step[1])
        if step[0] == 'forward':
            hor += x
        elif step[0] == 'down':
            ver += x
        else:
            ver -= x
    print(hor * ver)


def part2():
    instr = read_file()
    hor = 0
    ver = 0
    aim = 0
    for step in instr:
        x = int(step[1])
        if step[0] == 'forward':
            hor += x
            ver += aim * x
        elif step[0] == 'down':
            aim += x
        else:
            aim -= x
    print(hor * ver)



if __name__ == '__main__':
#    part1()
    part2()
