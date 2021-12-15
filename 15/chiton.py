import heapq
from collections import defaultdict

from rich import print


def get_input():
    input = {}
    with open("input.txt") as input_txt:
        for x, line in enumerate(input_txt):
            for i, n in enumerate(line.strip()):
                input[(i, x)] = int(n)
    return input


def dijkstra(grid):
    destination = defaultdict(lambda: float('inf'))
    nodes = [(0, (0, 0))]
    while len(nodes) > 0:
        point, (i, n) = heapq.heappop(nodes)
        for node in ((i, n + 1), (i, n - 1), (i + 1, n), (i - 1, n)):
            if node not in grid:
                continue

            points = point + grid[node]
            if points < destination[node]:
                destination[node] = points
                heapq.heappush(nodes, (points, node))

    return destination[max(destination.keys())]


def part_1(input):
    return dijkstra(input)


def part_2(input):
    width, height = max(input.keys())
    height += 1
    width += 1

    map = input.copy()
    for first in range(5):
        for second in range(5):
            total = first + second
            if total == 0:
                continue

            for (i, n), points in input.items():
                value = points + total
                if value > 9:
                    value -= 9
                map[(i + (second * width), n + (first * height))] = value

    return dijkstra(map)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
