from collections import defaultdict

from rich import print


def get_input():
    state = []
    rules = {}
    with open("input.txt") as input_txt:
        for line in input_txt:
            if len(line) > 2 and "->" not in line:
                state = list(line.strip())
            if "->" in line:
                pair, insert = line.strip().split(" -> ")
                pair = tuple(pair)
                rules[pair] = insert

    return (state, rules)


def submarine_polymer(template, rules, iteration):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pair = tuple(template[i:i + 2])
        pairs[pair] += 1

    for _ in range(iteration):
        next = defaultdict(int)
        for pair, count in pairs.items():
            if pair in rules:
                insert = rules[pair]
                next[(pair[0], insert)] += count
                next[(insert, pair[1])] += count
            else:
                next[pair] += count
        pairs = next

    counts = defaultdict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count
    counts[template[-1]] += 1

    most_common = 0
    least_common = float('inf')
    for count in counts.values():
        most_common = max(most_common, count)
        least_common = min(least_common, count)
    return most_common - least_common


def part_1(template, rules):
    return submarine_polymer(template, rules, 10)


def part_2(template, rules):
    return submarine_polymer(template, rules, 40)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(*input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(*input)
    print(f"Puzzle Part 2: {part_2}")
