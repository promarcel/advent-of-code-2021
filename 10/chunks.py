from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def part_1(input):
    score = 0
    for line in input:
        chunk = []
        for c in line:
            closable = chunk[-1] if len(chunk) > 0 else None
            if c in '[{(<':
                chunk.append(c)
            elif closable == "<" and c == ">":
                chunk.pop()
            elif closable == "{" and c == "}":
                chunk.pop()
            elif closable == "(" and c == ")":
                chunk.pop()
            elif closable == "[" and c == "]":
                chunk.pop()
            else:
                score += scores[c]
                break

    return score


completion_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def part_2(input):
    line_scores = []
    for line in input:
        corrupt = False
        chunk = []
        for c in line:
            closable = chunk[-1] if len(chunk) > 0 else None
            if c in '[{(<':
                chunk.append(c)
            elif closable == "<" and c == ">":
                chunk.pop()
            elif closable == "{" and c == "}":
                chunk.pop()
            elif closable == "(" and c == ")":
                chunk.pop()
            elif closable == "[" and c == "]":
                chunk.pop()
            else:
                corrupt = True
                break

        if corrupt:
            continue

        score = 0
        for symbol in reversed(chunk):
            score = score * 5 + completion_scores[symbol]

        line_scores.append(score)

    line_scores.sort()
    mid = line_scores[len(line_scores) // 2]
    return mid


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
