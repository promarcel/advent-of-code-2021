from collections import defaultdict

from rich import print


def get_input():
    input = defaultdict(lambda: -1000000)
    with open("input.txt") as input_txt:
        i = 0
        for i, line in enumerate(input_txt):
            for j, c in enumerate(line.strip()):
                input[(i, j)] = int(c)
    return input


def incr(coord, state):
    state[coord] += 1
    flash = 0
    if state[coord] == 10:
        i, j = coord
        flash = 1
        flash += incr((i + 1, j), state)
        flash += incr((i + 1, j + 1), state)
        flash += incr((i + 1, j - 1), state)
        flash += incr((i - 1, j), state)
        flash += incr((i - 1, j + 1), state)
        flash += incr((i - 1, j - 1), state)
        flash += incr((i, j + 1), state)
        flash += incr((i, j - 1), state)

    return flash


def flash_progress(state):
    flash = 0
    for coord in list(state.keys()):
        flash += incr(coord, state)

    for coord in list(state.keys()):
        if state[coord] >= 10:
            state[coord] = 0
    return flash


def part_1(input):
    state = input.copy()
    flash = 0
    for turn in range(100):
        flash += flash_progress(state)
    return flash


def part_2(input):
    state = input.copy()
    turn = 1
    while True:
        do_flash = flash_progress(state)
        if do_flash == 100:
            return turn
        turn += 1


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
