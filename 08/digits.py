from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            patterns, outputs = line.strip().split("|")
            patterns = patterns.split(" ")
            outputs = outputs.strip().split(" ")
            input.append((patterns, outputs))
    return input


def part_1(input):
    count = 0
    for _, outputs in input:
        for output in outputs:
            if len(output) in (2, 3, 4, 7):
                count += 1

    return count


def do_join(letters):
    return "".join(sorted(letters))


SEGMENTS = set("abcdefg")


def part_2(input):
    total = 0
    for patterns, outputs in input:
        decoder = {}
        right = None
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        while len(decoder) < 9:
            for pattern in patterns:
                pattern = do_join(pattern)
                if pattern in decoder:
                    continue

                if len(pattern) == 2:
                    right = set(pattern)
                    decoder[pattern] = 1

                elif len(pattern) == 3 and right is not None:
                    a = set(pattern).difference(right).pop()
                    decoder[pattern] = 7

                elif len(pattern) == 6 and right is not None and len(right.difference(pattern)) == 1:
                    c = right.difference(pattern).pop()
                    f = right.difference(set([c])).pop()
                    decoder[pattern] = 6

                elif len(pattern) == 5 and c is not None and c not in pattern:
                    e = SEGMENTS.difference(pattern).difference([c]).pop()
                    decoder[pattern] = 5

                elif len(
                        pattern) == 5 and c is not None and c in pattern and e is not None and e in pattern and f is not None and f not in pattern:
                    b = SEGMENTS.difference(pattern).difference([f]).pop()
                    decoder[pattern] = 2

                elif len(pattern) == 7:
                    decoder[pattern] = 8

                elif len(
                        pattern) == 5 and c is not None and c in pattern and f is not None and f in pattern and b is not None and b not in pattern:
                    e = SEGMENTS.difference(pattern).difference([b]).pop()
                    decoder[pattern] = 3

                elif len(pattern) == 6 and e is not None and e not in pattern:
                    decoder[pattern] = 9

                elif len(pattern) == 4:
                    decoder[pattern] = 4

        value = 0
        for i, output in enumerate(outputs):
            power = 3 - i
            value += decoder.get(do_join(output), 0) * (10 ** power)

        total += value
    return total


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
