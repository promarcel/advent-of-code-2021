from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(int(line))
    return input


def part_1(input):
    count = 0
    for i, value in enumerate(input):
        if i == 0:
            continue

        if value > input[i - 1]:
            count += 1
    return count


def part_2(input):
    previous = 100000000
    count = 0
    for i in range(2, len(input)):
        total = input[i] + input[i - 1] + input[i - 2]
        if total > previous:
            count += 1
        previous = total
    return count


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
