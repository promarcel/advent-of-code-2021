from collections import defaultdict

from rich import print


def get_input():
    input = defaultdict(set)
    with open("input.txt") as input_txt:
        for line in input_txt:
            node = line.strip().split("-")
            input[node[0]].add(node[1])
            input[node[1]].add(node[0])
    return input


def traverse(neighbor, node, state):
    if node == "end":
        return 1

    paths = 0
    next = state.copy()
    next.add(node)
    for next_candidate in neighbor[node]:
        if next_candidate in state and not next_candidate.isupper():
            continue
        paths += traverse(neighbor, next_candidate, next)
    return paths


def part_1(neighbor):
    return traverse(neighbor, "start", set())


def traverse_x2(neighbors, node, previous):
    if node == "end":
        return 1

    next = previous.copy()
    if node.islower():
        next[node] = next.get(node, 0) + 1

    is_done = any(visits >= 2 for visits in next.values())
    paths = 0
    for candidate_next in neighbors[node]:
        if candidate_next == "start":
            continue
        elif next.get(candidate_next, 0) >= 1 and is_done:
            continue
        paths += traverse_x2(neighbors, candidate_next, next)
    return paths


def part_2(neighbor):
    return traverse_x2(neighbor, "start", {})


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
