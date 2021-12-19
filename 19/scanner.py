from itertools import permutations, product

import numpy
from rich import print


def get_input():
    with open('input.txt') as input_txt:
        input = input_txt.read().split('\n\n')
    return input


AXES = [numpy.array(permutation) for permutation in permutations([1, 2, 3])]
DIRECTIONS = [numpy.array(prod) for prod in product([-1, 1], [-1, 1], [-1, 1])]
ARGUMENTS = [(axis, direction) for axis, direction in product(AXES, DIRECTIONS)]


class Scanner:
    def __init__(self, nodes: str):
        lines = nodes.splitlines()
        self.nodes = numpy.array([[int(x) for x in l.split(',')] for l in lines[1:]], dtype='int16')
        self.position = None

    def offset(self, other: 'Scanner'):
        if other.position is not None: return False
        node = self.nodes
        for coords, direction in ARGUMENTS:
            other_points_cp = other.nodes[:, coords - 1] * direction
            direction = node[numpy.newaxis, :] - other_points_cp[:, numpy.newaxis]
            uniques = [numpy.unique(direction[..., i], return_counts=True) for i in range(3)]

            if all([max(unique[1]) >= 12 for unique in uniques]):
                other.nodes = other_points_cp
                other.position = numpy.array([unique[0][unique[1] >= 12][0] for unique in uniques],
                                             dtype='int16') + self.position
                return True

        return False


def part_1(input):
    scanners = [Scanner(node) for node in input]
    scanners[0].position = numpy.array([0, 0, 0])

    while any(scanner.position is None for scanner in scanners):
        for n in filter(lambda x: x.position is None, scanners):
            for coords in scanners:
                if coords.position is not None and coords.offset(n):
                    break

    beacons = set()
    for scanner in scanners:
        for node in (scanner.nodes + scanner.position):
            beacons.add(tuple(node))

    return len(beacons), scanners


def part_2(input):
    distance = 0
    for scanner_1 in input:
        for scanner_2 in input:
            if scanner_1 is not scanner_2:
                distance = numpy.abs(scanner_1.position - scanner_2.position).sum()
                distance = max(distance, distance)
    return distance


if __name__ == "__main__":
    input = get_input()

    part_1, part_2_input = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(part_2_input)
    print(f"Puzzle Part 2: {part_2}")
