from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def part_1(input):
    bit_count = [0] * len(input[0])
    for binary_string in input:
        for i, one_or_zero in enumerate(binary_string):
            bit_count[i] += int(one_or_zero)

    gamma_string = ""
    epsilon_string = ""
    for bit in bit_count:
        if bit > (len(input) / 2):
            gamma_string = gamma_string + "1"
            epsilon_string = epsilon_string + "0"
        else:
            gamma_string = gamma_string + "0"
            epsilon_string = epsilon_string + "1"

    gamma = int(gamma_string, base=2)
    epsilon = int(epsilon_string, base=2)

    return gamma * epsilon


def filtermagic(numbers, use_most_common, bit=0):
    assert len(numbers) != 0
    if len(numbers) == 1:
        return numbers[0]

    ones_count = 0
    for number in numbers:
        ones_count += int(number[bit])

    most_common = 1 if ones_count >= (len(numbers) / 2) else 0
    value = most_common if use_most_common else (most_common + 1) % 2
    value = str(value)

    filtered = [n for n in numbers if n[bit] == value]
    return filtermagic(filtered, use_most_common, bit=bit + 1)


def part_2(input):
    oxygen = int(filtermagic(input, True), base=2)
    co2 = int(filtermagic(input, False), base=2)
    return oxygen * co2


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
