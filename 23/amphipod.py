import copy

import numpy


def get_input():
    with open("input.txt") as input_txt:
        lines = input_txt.read().split('\n')
        lines = lines[2:]
        _, _, _, c11, c12, c13, c14, _, _, _ = lines[0].split('#')
        _, c21, c22, c23, c24, _, = lines[1].split('#')
        chambers = [[c11, c21], [c12, c22], [c13, c23], [c14, c24]]
        hallway = [' '] * 11
    return chambers, hallway


def moves(chambers, hallway, chamber_length, chamber_nr):
    hallway_index = 2 * (chamber_nr + 1)

    out = []

    amphi = chambers[chamber_nr].pop(0)
    total_moves = chamber_length - len(chambers[chamber_nr])

    for i in range(1, len(hallway) - hallway_index):
        if hallway_index + i in [2, 4, 6, 8]:
            continue
        if hallway[hallway_index + i] == ' ':
            new_hallway = copy.deepcopy(hallway)
            new_hallway[hallway_index + i] = amphi
            out.append((amphi, chambers, new_hallway, total_moves + i, hallway_index + i))
        else:
            break

    for i in range(-1, -hallway_index - 1, -1):
        if hallway_index + i in [2, 4, 6, 8]:
            continue
        if hallway[hallway_index + i] == ' ':
            new_hallway = copy.deepcopy(hallway)
            new_hallway[hallway_index + i] = amphi
            out.append((amphi, chambers, new_hallway, total_moves + abs(i), hallway_index + i))
        else:
            break
    return out


def goto(hallway, i1, i2):
    sign = 1 if i2 > i1 else -1
    can_go = True
    for i in range(i1 + sign, i2 + sign, sign):
        can_go = can_go and hallway[i] == ' '
    return can_go


def list(l):
    tup = tuple([tuple(c) for c in l])
    return tup


cache = dict()


def recursive(chambers, hallway, chamber_length):
    cost_map = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    desired = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    total_cost = 0
    hallway_modified = True
    while hallway_modified:
        hallway_modified = False
        possible = []
        for i in range(len(hallway)):
            c = hallway[i]
            if c != ' ':
                desired_room = desired[c]
                hallway_index = 2 * (desired_room + 1)
                if chambers[desired_room] == len(chambers[desired_room]) * [c] and goto(hallway, i, hallway_index):
                    nr_moves = abs(hallway_index - i) + chamber_length - len(chambers[desired_room])
                    possible.append([i, desired_room, cost_map[c] * nr_moves])
                    break

        if len(possible) > 0:
            possible = sorted(possible, key=lambda x: x[2])

            idx, desired_room, cost = possible[0]
            total_cost += cost
            chambers[desired_room] = [hallway[idx]] + chambers[desired_room]
            hallway[idx] = ' '
            hallway_modified = True

    moves = []
    for i in range(len(chambers)):
        chamber = chambers[i]
        desired_amphi = desired[i]
        if chamber != len(chamber) * [desired_amphi]:
            moves += moves(copy.deepcopy(chambers), copy.deepcopy(hallway), chamber_length, i)

    moves = sorted(moves, key=lambda x: (x[3] + abs(x[4] - 2 * (desired[x[0]] + 1))) * cost_map[
        x[0]])

    new_cost = numpy.inf
    if chambers == [['A'] * chamber_length, ['B'] * chamber_length, ['C'] * chamber_length, ['D'] * chamber_length]:
        new_cost = 0
    for amphi, new_c, new_h, nr_moves, _ in moves:
        if (list(new_c), tuple(new_h)) in cache:
            cost = cache[list(new_c), tuple(new_h)] + nr_moves * cost_map[amphi]
            new_cost = min(new_cost, cost)
        else:
            cost = recursive(copy.deepcopy(new_c), copy.deepcopy(new_h))
            cache[list(new_c), tuple(new_h)] = cost
            new_cost = min(new_cost, cost + nr_moves * cost_map[amphi])

    return total_cost + new_cost


def part_1(chambers, hallway, chamber_length):
    return recursive(chambers, hallway, chamber_length)


def part_2(chambers, hallway, chamber_length):
    chambers[0] = [chambers[0][0], 'D', 'D', chambers[0][1]]
    chambers[1] = [chambers[1][0], 'C', 'B', chambers[1][1]]
    chambers[2] = [chambers[2][0], 'B', 'A', chambers[2][1]]
    chambers[3] = [chambers[3][0], 'A', 'C', chambers[3][1]]

    return recursive(chambers, hallway, chamber_length)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(*input, 2)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(*input, 4)
    print(f"Puzzle Part 2: {part_2}")
