from typing import Dict, List


symbols = set("*%#@+-=/&$")


def part_one():
    with open("./inputs/3.txt") as f:
        lines = f.readlines()
        part_numbers: List[int] = []
        for i in range(len(lines)):
            line = lines[i]

            # keep track of the current number
            cur_number = ""
            # and whether it's adjacent to a symbol
            adjacent = False

            for j in range(len(line)):
                char = line[j]
                if char.isdigit():
                    cur_number += char

                    # look around for a symbol
                    if (
                        (j > 0 and i > 0 and lines[i - 1][j - 1] in symbols)
                        or (lines[i - 1][j] in symbols)
                        or (j < len(line) - 1 and lines[i - 1][j + 1] in symbols)
                        or (j > 0 and line[j - 1] in symbols)
                        or (j < len(line) - 1 and line[j + 1] in symbols)
                        or (
                            i < len(lines) - 1
                            and j > 0
                            and lines[i + 1][j - 1] in symbols
                        )
                        or (i < len(lines) - 1 and lines[i + 1][j] in symbols)
                        or (
                            i < len(lines) - 1
                            and j < len(line) - 1
                            and lines[i + 1][j + 1] in symbols
                        )
                    ):
                        adjacent = True
                        continue
                else:
                    # commit the complete part number
                    if cur_number != "" and adjacent:
                        part_numbers.append(int(cur_number))
                    cur_number = ""
                    adjacent = False

            # commit the complete part number
            if cur_number != "" and adjacent:
                part_numbers.append(int(cur_number))

        print(sum(part_numbers))


def part_two():
    with open("./inputs/3.txt") as f:
        lines = f.readlines()

        # keep track of gear location to list of part numbers
        # later, loop over and multiple the lists of length two
        gears: Dict[str, List[int]] = {}

        # lil helper
        def add_to_gears(loc: str, num: int):
            if loc in gears:
                gears[loc].append(num)
            else:
                gears[loc] = [num]

        for i in range(len(lines)):
            line = lines[i]
            cur_number = ""
            adjacent = False

            # keep track of the nearby gears so we register
            # the current part number with the gear location
            nearby_gears = set()

            for j in range(len(line)):
                char = line[j]
                if char.isdigit():
                    cur_number += char

                    if (
                        (j > 0 and i > 0 and lines[i - 1][j - 1] in symbols)
                        or (lines[i - 1][j] in symbols)
                        or (j < len(line) - 1 and lines[i - 1][j + 1] in symbols)
                        or (j > 0 and line[j - 1] in symbols)
                        or (j < len(line) - 1 and line[j + 1] in symbols)
                        or (
                            i < len(lines) - 1
                            and j > 0
                            and lines[i + 1][j - 1] in symbols
                        )
                        or (i < len(lines) - 1 and lines[i + 1][j] in symbols)
                        or (
                            i < len(lines) - 1
                            and j < len(line) - 1
                            and lines[i + 1][j + 1] in symbols
                        )
                    ):
                        adjacent = True

                    # from a part number digit's POV, look around for a gear
                    if j > 0 and i > 0 and lines[i - 1][j - 1] == "*":
                        nearby_gears.add(f"{i-1},{j-1}")
                    elif lines[i - 1][j] == "*":
                        nearby_gears.add(f"{i-1},{j}")
                    elif j < len(line) - 1 and lines[i - 1][j + 1] == "*":
                        nearby_gears.add(f"{i-1},{j+1}")
                    elif j > 0 and line[j - 1] == "*":
                        nearby_gears.add(f"{i},{j-1}")
                    elif j < len(line) - 1 and line[j + 1] == "*":
                        nearby_gears.add(f"{i},{j+1}")
                    elif i < len(lines) - 1 and j > 0 and lines[i + 1][j - 1] == "*":
                        nearby_gears.add(f"{i+1},{j-1}")
                    elif i < len(lines) - 1 and lines[i + 1][j] == "*":
                        nearby_gears.add(f"{i+1},{j}")
                    elif (
                        i < len(lines) - 1
                        and j < len(line) - 1
                        and lines[i + 1][j + 1] == "*"
                    ):
                        nearby_gears.add(f"{i+1},{j+1}")
                else:
                    # register part number with gear locations
                    if cur_number != "" and adjacent:
                        for loc in nearby_gears:
                            add_to_gears(loc, int(cur_number))
                    cur_number = ""
                    adjacent = False
                    nearby_gears = set()

            # register part number with gear locations
            if cur_number != "" and adjacent:
                for loc in nearby_gears:
                    add_to_gears(loc, int(cur_number))

        print(
            sum([nums[0] * nums[1] if len(nums) == 2 else 0 for nums in gears.values()])
        )


if __name__ == "__main__":
    part_one()
    part_two()
