def read_file():
    with open('input.txt', 'r') as file:
        lines = [list(line.strip()) for line in file]
    return lines

def part1():
    mult = 1
    gamma = 0
    epsilon = 0
    report = read_file()
    threshold = len(report)
    binlen = len(report[0])
    for pos in range(0, binlen):
        onecount = 0
        for rep in report:
            if rep[binlen-1-pos] == '1':
                onecount += 1
        if onecount > threshold/2:
            gamma += mult
        else:
            epsilon += mult
        mult *= 2
    print(gamma*epsilon)
            

# return the common list and uncommon list given position (com=True: common, com=False, uncommon)
def find_cu(binlst, pos, com):
    zero = []
    one = []
    threshold = len(binlst)  # threshold to become the most common bit
    onecount = 0
    for rep in binlst:
        if rep[pos] == '1':
            onecount += 1
            one.append(rep)
        else:
            zero.append(rep)
    if com:
        if onecount >= threshold-onecount:
            return one
        return zero
    else:
        if onecount < threshold-onecount:
            return one 
        return zero


def part2():
    report = read_file()
    ox_pos = 0
    co_pos = 0
    ox = find_cu(report, ox_pos, True)
    co = find_cu(report, co_pos, False)
    while(len(ox) > 1):
        ox_pos += 1
        ox = find_cu(ox, ox_pos, True)
    while(len(co) > 1):
        co_pos += 1
        co = find_cu(co, co_pos, False)
    ox = ox[0]
    co = co[0]
    oxy = 0
    co2 = 0
    ind = len(report[0])-1
    mult = 1
    while(ind > -1):
        if ox[ind] == '1':
            oxy += mult
        if co[ind] == '1':
            co2 += mult
        mult *= 2
        ind -= 1
    print(oxy * co2)


if __name__ == '__main__':
    part1()
    part2()
