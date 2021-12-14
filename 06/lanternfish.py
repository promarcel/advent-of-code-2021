from collections import defaultdict

from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.extend([int(n) for n in line.split(",")])
    return input


def part_1(input):
    ages = input
    for i in range(80):
        next = []
        for age in ages:
            if age == 0:
                next.append(6)
                next.append(8)

            else:
                next.append(age - 1)

        ages = next
    return len(ages)


def part_2(input):
    age_buckets = defaultdict(int)
    for age in input:
        age_buckets[age] += 1

    for i in range(256):
        next_buckets = defaultdict(int)
        for i in range(9):
            fish = age_buckets.get(i, 0)
            if i == 0:
                next_buckets[8] += fish
                next_buckets[6] += fish

            else:
                next_buckets[i - 1] += fish

        age_buckets = next_buckets
    return sum(age_buckets.values())


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
