from collections import defaultdict

from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            source_str, dest_str = line.split("->")
            source = tuple(map(int, source_str.split(",")))
            dest = tuple(map(int, dest_str.split(",")))
            input.append((source, dest))
    return input


def puzzle(input, diagonals):
    grid = defaultdict(int)
    for source, dest in input:
        if not diagonals and source[0] != dest[0] and source[1] != dest[1]:
            continue

        x = dest[0] - source[0]
        dx = x // abs(x) if x != 0 else 0

        y = dest[1] - source[1]
        dy = y // abs(y) if y != 0 else 0

        last = source
        grid[source] += 1
        while last != dest:
            next = (last[0] + dx, last[1] + dy)
            grid[next] += 1
            last = next
    return len([v for v in grid.values() if v > 1])


def part_1(input):
    return puzzle(input, diagonals=False)


def part_2(input):
    return puzzle(input, diagonals=True)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
