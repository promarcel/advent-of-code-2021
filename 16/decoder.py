from functools import reduce

from rich import print


def get_input():
    input = ""
    with open("input.txt") as input_txt:
        for line in input_txt:
            input = format(int(line.strip(), 16), f'0>{len(line.strip()) * 4}b')
    return input


def bitstream(input):
    version = int(input[0:3], 2)
    total = version
    id = int(input[3:6], 2)
    n = 6
    value = None
    if id == 4:
        end = False
        bits = ""
        while not end:
            end = input[n] == "0"
            bits += input[n + 1:n + 5]
            n += 5

        value = int(bits, 2)
    else:
        length = input[6]
        n += 1
        store = []
        if length == "0":
            total_length = int(input[7:7 + 15], 2)
            n += 15
            end = n + total_length
            while n < end:
                count = bitstream(input[n:])
                store.append(count)
                count_version, count_length, _ = count
                n += count_length
                total += count_version
        elif length == "1":
            n += 11
            total = int(input[7:7 + 11], 2)
            for _ in range(total):
                count = bitstream(input[n:])
                store.append(count)
                count_version, count_length, _ = count
                n += count_length
                total += count_version
        else:
            raise Exception()

        values = [info[2] for info in store]
        if id == 0:
            value = sum(values)
        if id == 1:
            value = reduce(lambda a, b: a * b, values)
        if id == 2:
            value = min(values)
        if id == 3:
            value = max(values)
        if id == 5:
            value = 1 if values[0] > values[1] else 0
        if id == 6:
            value = 1 if values[0] < values[1] else 0
        if id == 7:
            value = 1 if values[0] == values[1] else 0

    assert value is not None
    return total, n, value


def part_1(input):
    return bitstream(input)[0]


def part_2(input):
    return bitstream(input)[2]


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
