from functools import reduce

from rich import print


def get_input():
    with open("input.txt") as input_txt:
        dot = set()
        fold = []
        for line in input_txt:
            if "," in line:
                coordinates = tuple(int(x) for x in line.strip().split(","))
                dot.add(coordinates)
            elif "=" in line:
                axis, coord = line.strip().split(" ")[-1].split("=")
                fold.append((axis, int(coord)))
    return (dot, fold)


def paperwork(dot, fold):
    axis, coord = fold
    folded = set()
    for x, y in dot:
        if axis == "x" and x > coord:
            x = coord - (x - coord)
        elif axis == "y" and y > coord:
            y = coord - (y - coord)
        folded.add((x, y))
    return folded


def part_1(dot, fold):
    return len(paperwork(dot, fold[0]))


def part_2(dot, fold):
    dot = reduce(paperwork, fold, dot)
    for y in range(7):
        for x in range(40):
            printing = "#" if (x, y) in dot else " "
            print(printing, end="")
        print("")


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(*input)
    print(f"Puzzle Part 1: {part_1}")

    print(f"Puzzle Part 2:")
    part_2(*input)
