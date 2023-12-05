from typing import List


def calc_score(line: str):
    _, numbers_text = line.split(":")
    winning_numbers_text, my_numbers_text = numbers_text.split("|")
    winning_numbers = set(winning_numbers_text.split())
    my_numbers = set(my_numbers_text.split())
    score = 0
    for n in my_numbers:
        if n in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score


def count_matching(line: str):
    _, numbers_text = line.split(":")
    winning_numbers_text, my_numbers_text = numbers_text.split("|")
    winning_numbers = set(winning_numbers_text.split())
    my_numbers = set(my_numbers_text.split())
    return len(winning_numbers.intersection(my_numbers))


def part_one():
    with open("./inputs/4.txt") as f:
        points = 0
        for line in f:
            points += calc_score(line)
        print(points)


def part_two():
    with open("./inputs/4.txt") as f:
        matches: List[int] = []
        for line in f:
            matches.append(count_matching(line))

        copies = [1 for _ in matches]
        for i in range(len(copies)):
            count = copies[i]
            for j in range(1, matches[i] + 1):
                copies[i + j] += count
        print(sum(copies))


if __name__ == "__main__":
    part_one()
    part_two()
