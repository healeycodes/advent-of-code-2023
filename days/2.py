from enum import Enum
import re
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def parse_color(s: str) -> Color:
    if "red" in s:
        return Color.RED
    elif "green" in s:
        return Color.GREEN
    elif "blue" in s:
        return Color.BLUE
    raise Exception(f"couldn't find color: {s}")


def possible_game(reveals: str, red_max: int, green_max: int, blue_max: int):
    """
    :reveals: e.g. `3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`
    """
    for reveal in reveals:
        for cubes in reveal.split(","):
            color, count = parse_color(cubes), int(re.search(r"\d+", cubes).group(0))
            if (
                color == Color.RED
                and count > red_max
                or color == Color.GREEN
                and count > green_max
                or Color.BLUE
                and count > blue_max
            ):
                return False
    return True


def fewest_cubes(reveals: str):
    """
    :reveals: e.g. `3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`
    """
    red_max, green_max, blue_max = [0, 0, 0]
    for reveal in reveals:
        for cubes in reveal.split(","):
            color, count = parse_color(cubes), int(re.search(r"\d+", cubes).group(0))
            if color == Color.RED:
                red_max = max(count, red_max)
            elif color == Color.BLUE:
                blue_max = max(count, blue_max)
            elif color == Color.GREEN:
                green_max = max(count, green_max)
    return (red_max, green_max, blue_max)


def part_one():
    with open("./inputs/2.txt") as f:
        game_ids: List[int] = []
        for line in f:
            start, end = line.split(":")

            game_id = re.search(r"\d+", start).group(0)
            if possible_game(end.split(";"), 12, 13, 14):
                game_ids.append(int(game_id))
        print(sum(game_ids))


def part_two():
    with open("./inputs/2.txt") as f:
        cube_powers: List[int] = []
        for line in f:
            _, end = line.split(":")

            min_cubes = fewest_cubes(end.split(";"))
            cube_powers.append(min_cubes[0] * min_cubes[1] * min_cubes[2])
        print(sum(cube_powers))


if __name__ == "__main__":
    part_one()
    part_two()
