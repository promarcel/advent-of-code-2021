from heapq import nlargest

from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append([int(c) for c in line.strip()])
    return input


def part_1(heightmap):
    risk_level = 0
    for i in range(len(heightmap)):
        row = heightmap[i]
        for j in range(len(heightmap[0])):
            height = heightmap[i][j]
            if j < len(row) - 1 and row[j + 1] <= height:
                continue
            if i > 0 and heightmap[i - 1][j] <= height:
                continue
            if j > 0 and heightmap[i][j - 1] <= height:
                continue
            if i < len(heightmap) - 1 and heightmap[i + 1][j] <= height:
                continue

            risk_level += height + 1

    return risk_level


def part_2(heightmap):
    sizes = []
    membership = set()
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            candidates = [(i, j)]
            basin_size = 0
            while len(candidates) > 0:
                candidate = candidates.pop()
                ci, cj = candidate
                if ci < 0 or ci >= len(heightmap):
                    continue
                if cj < 0 or cj >= len(heightmap[0]):
                    continue
                if heightmap[ci][cj] >= 9:
                    continue
                if candidate in membership:
                    continue

                basin_size += 1
                membership.add(candidate)
                candidates.append((ci + 1, cj))
                candidates.append((ci - 1, cj))
                candidates.append((ci, cj + 1))
                candidates.append((ci, cj - 1))

            if basin_size > 0:
                sizes.append(basin_size)

    largest = list(nlargest(3, sizes))

    return largest[0] * largest[1] * largest[2]


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
