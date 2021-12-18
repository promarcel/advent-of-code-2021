import json
from functools import reduce
from itertools import permutations
from math import ceil

from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(json.loads(line))
    return input


def number(list, parent=None):
    if type(list) == int:
        return RegularNumber(list, parent)
    else:
        return Number(list, parent)


class Number():
    def __init__(self, list, parent):
        self.parent = parent
        self.left = number(list[0], self)
        self.right = number(list[1], self)

    def is_pair(self):
        return True

    def can_explode(self):
        nested_level = 0
        curs = self
        while curs.parent is not None:
            curs = curs.parent
            nested_level += 1
        result = nested_level == 4

        return result

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __str__(self):
        return f"[{self.left},{self.right}]"


class RegularNumber(Number):
    def __init__(self, list, parent):
        self.parent = parent
        self.value = list

    def is_pair(self):
        return False

    def magnitude(self):
        return self.value

    def __str__(self):
        return str(self.value)


def explode_number(number):
    leaves = []
    nodes = [number]
    exploding_node = None
    while len(nodes) > 0:
        position = nodes.pop()

        if type(position) == RegularNumber:
            leaves.append(position)
            continue

        nodes.append(position.right)
        nodes.append(position.left)
        if exploding_node is None and position.can_explode():
            exploding_node = position

    if exploding_node is not None:
        left_index = leaves.index(exploding_node.left)
        if left_index > 0:
            leaves[left_index - 1].value += exploding_node.left.value

        right_index = left_index + 1
        if right_index < len(leaves) - 1:
            leaves[right_index + 1].value += exploding_node.right.value

        parent = exploding_node.parent
        if parent.left is exploding_node:
            parent.left = RegularNumber(0, parent)
        elif parent.right is exploding_node:
            parent.right = RegularNumber(0, parent)
        else:
            raise Exception("Exploding Node")

    return exploding_node is not None


def split_number(number):
    nodes = [number]
    while len(nodes) > 0:
        position = nodes.pop()

        if type(position) == RegularNumber and position.value >= 10:
            parent = position.parent
            if parent.left is position:
                parent.left = Number([position.value // 2, ceil(position.value / 2)], parent)
            elif parent.right is position:
                parent.right = Number([position.value // 2, ceil(position.value / 2)], parent)
            return True
        elif type(position) == RegularNumber:
            continue

        nodes.append(position.right)
        nodes.append(position.left)

    return False


def reduce_number(number):
    action = True
    while action:
        action = explode_number(number) or split_number(number)
    return number


def add(a, b):
    total = Number([0, 0], None)
    total.left = a
    total.right = b
    a.parent = total
    b.parent = total
    return reduce_number(total)


def part_1(input):
    total = reduce(add, [number(j) for j in input])
    return total.magnitude()


def part_2(input):
    return max(add(number(a), number(b)).magnitude() for a, b in permutations(input, 2))


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
