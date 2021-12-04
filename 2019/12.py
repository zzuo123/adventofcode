import re
import collections

position = {}
velocity = {}


def init():
    with open('12.txt', 'r') as file:
        for index, line in enumerate(file):
            match_obj = re.match(r"<x=(-?[0-9]*), y=(-?[0-9]*), z=(-?[0-9]*)>", line)
            position[index] = {0: int(match_obj.group(1)), 1: int(match_obj.group(2)), 2: int(match_obj.group(3))}
    for index in range(4):
        velocity[index] = {0: 0, 1: 0, 2: 0}


def apply_gravity(dim_index):
    for moon_index in range(4):
        vel_change = 0
        for other_index in range(4):
            if other_index != moon_index:
                if position[other_index][dim_index] > position[moon_index][dim_index]:
                    vel_change += 1
                elif position[other_index][dim_index] < position[moon_index][dim_index]:
                    vel_change -= 1
        velocity[moon_index][dim_index] += vel_change


def apply_velocity(dim_index):
    for moon_index in range(4):
        position[moon_index][dim_index] += velocity[moon_index][dim_index]


init()
for i in range(1000):
    for dim in range(3):
        apply_gravity(dim)
        apply_velocity(dim)

total = 0
for i in range(4):
    pot = 0
    kin = 0
    for j in range(3):
        pot += abs(position[i][j])
        kin += abs(velocity[i][j])
    total += pot * kin

print(total)

# ------------------ part 2 ------------------------
init()
# x, y, z history
history = {0: {0: [], 1: 0}, 1: {0: [], 1: 0}, 2: {0: [], 1: 0}}


def find(dimension):
    apply_gravity(dimension)
    apply_velocity(dimension)
    positions = [position[0][dimension], position[1][dimension], position[2][dimension], position[3][dimension]]
    while positions not in history[dimension][0]:
        history[dimension][0].append(positions)
        history[dimension][1] += 1
        apply_gravity(dimension)
        apply_velocity(dimension)
        positions = [position[0][dimension], position[1][dimension], position[2][dimension], position[3][dimension]]
    return history[dimension][1]


results = [find(0), find(1), find(2)]
while results[0] != results[1] or results[1] != results[2]:
    ind = results.index(min(results))
    print(ind, results)
    results[ind] = find(ind)

print(results[0], results[1], results[2])
