def match_number(s: str) -> str | None:
    if s.startswith("one"):
        return "1"
    elif s.startswith("two"):
        return "2"
    elif s.startswith("three"):
        return "3"
    elif s.startswith("four"):
        return "4"
    elif s.startswith("five"):
        return "5"
    elif s.startswith("six"):
        return "6"
    elif s.startswith("seven"):
        return "7"
    elif s.startswith("eight"):
        return "8"
    elif s.startswith("nine"):
        return "9"


def part_one():
    calibration_values: int = []
    with open("./inputs/1.txt") as f:
        for line in f:
            number = ""

            # first digit
            for i in range(0, len(line)):
                cur_digit = line[i]
                if cur_digit.isdigit():
                    number += cur_digit
                    break

            # last digit
            for i in range(len(line) - 1, -1, -1):
                cur_digit = line[i]
                if cur_digit.isdigit():
                    number += cur_digit
                    break

            calibration_values.append(int(number))
    print(sum(calibration_values))


def part_two():
    calibration_values: int = []
    with open("./inputs/1.txt") as f:
        for line in f:
            number = ""

            # first digit
            for i in range(0, len(line)):
                cur_digit = line[i]
                if cur_digit.isdigit():
                    number += cur_digit
                    break
                number_match = match_number(line[i:])
                if number_match:
                    number += number_match
                    break

            # last digit
            for i in range(len(line) - 1, -1, -1):
                cur_digit = line[i]
                if cur_digit.isdigit():
                    number += cur_digit
                    break
                number_match = match_number(line[i:])
                if number_match:
                    number += number_match
                    break

            calibration_values.append(int(number))
    print(sum(calibration_values))


if __name__ == "__main__":
    part_one()
    part_two()
