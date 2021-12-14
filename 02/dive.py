from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            direction, amount = line.split()
            input.append((direction, int(amount)))
    return input


def part_1(input):
    forward = 0
    depth = 0
    for direction, amount in input:
        if direction == "forward":
            forward += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    return forward * depth


def part_2(input):
    forward = 0
    depth = 0
    aim = 0
    for direction, amount in input:
        if direction == "forward":
            forward += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return forward * depth


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
