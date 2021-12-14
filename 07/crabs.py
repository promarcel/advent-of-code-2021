from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.extend(list(map(int, line.split(","))))
    return input


def cost_target(locations, target):
    return sum((abs(location - target) for location in locations))


def part_1(locations):
    best = 100000000000
    for i in range(min(locations), max(locations)):
        cost = sum((abs(location - i) for location in locations))
        best = min(cost, best)

    return best


def part_2(locations):
    best = 100000000000
    for i in range(min(locations), max(locations)):
        cost = sum(((abs(location - i) + 1) * abs(location - i) // 2 for location in locations))
        best = min(cost, best)

    return best


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
