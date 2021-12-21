import itertools

from rich import print


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().rstrip().split('\n')
        player_1 = input[0].split(": ")[1]
        player_2 = input[1].split(": ")[1]
    return int(player_1) - 1, int(player_2) - 1


leaderboard = {}


def scores(state):
    player_1, player_2, score_1, score_2 = state
    if score_1 >= 21: return (1, 0)
    if score_2 >= 21: return (0, 1)
    if (state) in leaderboard: return leaderboard[(state)]

    total_scores = (0, 0)

    for die in itertools.product([1, 2, 3], repeat=3):
        new_player_1 = (player_1 + sum(die)) % 10
        new_player_2 = score_1 + new_player_1 + 1

        account_score_1, account_score_2 = scores((player_2, new_player_1, score_2, new_player_2))
        total_scores = (total_scores[0] + account_score_2, total_scores[1] + account_score_1)

    leaderboard[(state)] = total_scores

    return total_scores


def part_1(player_1, player_2):
    score_1 = score_2 = 0
    life = 0

    while True:
        round_1 = life * 3 + 6
        life += 3
        player_1 = (player_1 + round_1) % 10
        score_1 += player_1 + 1
        if score_1 >= 1000: break

        round_2 = life * 3 + 6
        life += 3
        player_2 = (player_2 + round_2) % 10
        score_2 += player_2 + 1
        if score_2 >= 1000: break

    return min(score_1, score_2) * life


def part_2(player_1, player_2):
    return max(scores((player_1, player_2, 0, 0)))


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(*input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(*input)
    print(f"Puzzle Part 2: {part_2}")
