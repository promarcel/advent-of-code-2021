from rich import print


class Board:
    def __init__(self):
        self._numbers = []
        self._hits = [[0] * 5 for _ in range(5)]
        self._membership = set()

    def add_row(self, numbers):
        self._numbers.append(numbers)
        self._membership.update(numbers)

    def is_bingo(self):
        for i in range(5):
            row = True
            column = True
            for j in range(5):
                row = row and self._hits[i][j] == 1
                column = column and self._hits[j][i] == 1

            if row or column:
                return True

        return False

    def mark(self, number):
        if number in self._membership:
            for i in range(5):
                for j in range(5):
                    if self._numbers[i][j] == number:
                        self._hits[i][j] = 1
                        break
            return True
        return False

    def score(self, win):
        total = 0
        for i in range(5):
            for j in range(5):
                if self._hits[i][j] == 0:
                    total += self._numbers[i][j]

        return total * win


def get_input():
    with open("input.txt") as input_txt:
        numbers = []
        boards = []
        first_line = True
        for line in input_txt:
            if first_line:
                numbers = [int(x) for x in line.split(",")]
                first_line = False
                continue

            if line.strip() == "":
                board = None
            elif board is None:
                board = Board()
                boards.append(board)
                board.add_row([int(x) for x in line.split()])
            else:
                board.add_row([int(x) for x in line.split()])

    return numbers, boards


def part_1(numbers, boards):
    for number in numbers:
        for board in boards:
            has_number = board.mark(number)
            if has_number and board.is_bingo():
                return board.score(number)
    return "There is no winner"


def part_2(numbers, boards):
    for number in numbers:
        for board in boards:
            has_number = board.mark(number)
            if has_number and len(boards) == 1 and board.is_bingo():
                return board.score(number)

        boards = [board for board in boards if not board.is_bingo()]
    return "No last board has been found"


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(*input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(*input)
    print(f"Puzzle Part 2: {part_2}")
