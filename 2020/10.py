with open('10.txt', 'r') as file:
    data = [int(line.strip()) for line in file]

data.sort()
data.insert(0, 0)
data.append(data[len(data) - 1] + 3)

# ---------------------------- part 1 ----------------------------
diff_count = {1: 0, 2: 0, 3: 0}
for i in range(1, len(data)):
    diff_count[data[i] - data[i - 1]] += 1
print(diff_count[1], diff_count[2], diff_count[3])
print(diff_count[1] * diff_count[3])


# ---------------------------- part2 ----------------------------


def find_ways(index):
    if index in found:
        return found[index]

    count = 0
    for next_ind in range(index + 1, index + 4):
        if next_ind < len(data) and data[next_ind] - data[index] <= 3:
            count += find_ways(next_ind)

    found[index] = count
    return count


found = {len(data) - 1: 1}
print(find_ways(0))
