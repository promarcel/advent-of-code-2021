from rich import print


def get_input():
    with open("input.txt") as input_txt:
        for line in input_txt:
            line = line.strip().split(': ')
            line = line[1].split(', ')
    return line


def steps(location, target):
    location_x, location_y = location
    x, y = location_x, location_y
    coords = [(x, y)]
    solved = False

    x_max = max(i[0] for i in target)
    x_min = min(i[0] for i in target)
    y_min = min(i[1] for i in target)
    y_max = max(i[1] for i in target)

    while (x < x_max and y > y_min) or (x > x_min and y < y_max):
        if (x, y) in target:
            solved = True
            break
        elif y < y_min:
            break
        if location_x > 0:
            location_x -= 1
        elif location_x < 0:
            location_x += 1
        location_y -= 1
        x += location_x
        y += location_y
        coords.append((x, y))
    if (x, y) in target:
        solved = True
    if (x, y) in target:
        solved = True
    if solved:
        return coords, max(x[1] for x in coords)
    return


def solve(input):
    target = []
    total = []
    found = set()
    for coord in input:
        x_start, x_end = map(int, coord[2:].split('..'))
        y_start, y_end = map(int, coord[2:].split('..'))
    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            target.append((x, y))
    for y in range(-300, 300):
        for x in range(300):
            result = steps((x, y), target)
            if result != False:
                total.append(result)
                found.add((x, y))
    max_value = max(n[1] for n in total)
    length = len(found)

    return max_value, length


if __name__ == "__main__":
    input = get_input()

    part_1, part_2 = solve(input)
    print(f"Puzzle Part 1: {part_1}")
    print(f"Puzzle Part 2: {part_2}")
