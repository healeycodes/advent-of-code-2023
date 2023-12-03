symbols = set("*%#@+-=/&$")

def part_one():
    with open('./inputs/3.txt') as f:
        lines = f.readlines()
        part_numbers: int = []
        for i in range(len(lines)):
            line = lines[i]
            cur_number = ''
            adjacent = False
            for j in range(len(line)):
                char = line[j]
                if char.isdigit():
                    cur_number += char
                    if (j > 0 and i > 0 and lines[i-1][j-1] in symbols) \
                        or (lines[i-1][j] in symbols) \
                        or (j < len(line) - 1 and lines[i-1][j+1] in symbols) \
                        or (j > 0 and line[j-1] in symbols) \
                        or (j < len(line) - 1 and line[j+1] in symbols) \
                        or (i < len(lines) - 1 and j > 0 and lines[i+1][j-1] in symbols) \
                        or (i < len(lines) - 1 and lines[i+1][j] in symbols) \
                        or (i < len(lines) - 1 and j < len(line) - 1 and lines[i+1][j+1] in symbols):
                        adjacent = True
                        continue 
                else:
                    if cur_number != '' and adjacent:
                        part_numbers.append(int(cur_number))
                    cur_number = ''
                    adjacent = False
            if cur_number != '' and adjacent:
                part_numbers.append(int(cur_number))
        print(sum(part_numbers))
                        

def part_two():
    with open('./inputs/3.txt') as f:
        lines = f.readlines()
        gears = {}

        def add_to_gears(loc: str, num: int):
            if loc in gears:
                gears[loc].append(num)
            else:
                gears[loc] = [num]

        for i in range(len(lines)):
            line = lines[i]
            cur_number = ''
            adjacent = False
            nearby_gears = set()
            for j in range(len(line)):
                char = line[j]
                if char.isdigit():
                    cur_number += char

                    if (j > 0 and i > 0 and lines[i-1][j-1] in symbols) \
                        or (lines[i-1][j] in symbols) \
                        or (j < len(line) - 1 and lines[i-1][j+1] in symbols) \
                        or (j > 0 and line[j-1] in symbols) \
                        or (j < len(line) - 1 and line[j+1] in symbols) \
                        or (i < len(lines) - 1 and j > 0 and lines[i+1][j-1] in symbols) \
                        or (i < len(lines) - 1 and lines[i+1][j] in symbols) \
                        or (i < len(lines) - 1 and j < len(line) - 1 and lines[i+1][j+1] in symbols):
                        adjacent = True
 
                    if (j > 0 and i > 0 and lines[i-1][j-1] == "*"):
                        nearby_gears.add(f'{i-1},{j-1}')
                    elif (lines[i-1][j] == "*"):
                        nearby_gears.add(f'{i-1},{j}')
                    elif (j < len(line) - 1 and lines[i-1][j+1]  == "*"):
                        nearby_gears.add(f'{i-1},{j+1}')
                    elif (j > 0 and line[j-1]  == "*"):
                        nearby_gears.add(f'{i},{j-1}')
                    elif (j < len(line) - 1 and line[j+1]  == "*"):
                        nearby_gears.add(f'{i},{j+1}')
                    elif (i < len(lines) - 1 and j > 0 and lines[i+1][j-1]  == "*"):
                        nearby_gears.add(f'{i+1},{j-1}')
                    elif (i < len(lines) - 1 and lines[i+1][j]  == "*"):
                        nearby_gears.add(f'{i+1},{j}')
                    elif (i < len(lines) - 1 and j < len(line) - 1 and lines[i+1][j+1]  == "*"):
                        nearby_gears.add(f'{i+1},{j+1}')
                else:
                    if cur_number != '' and adjacent:
                        for loc in nearby_gears:
                            add_to_gears(loc, int(cur_number))
                    cur_number = ''
                    adjacent = False
                    nearby_gears = set()
            if cur_number != '' and adjacent:
                for loc in nearby_gears:
                    add_to_gears(loc, int(cur_number))

        print(sum([nums[0] * nums[1] if len(nums) == 2 else 0 for nums in gears.values()]))

if __name__ == '__main__':
    part_one()
    part_two()
