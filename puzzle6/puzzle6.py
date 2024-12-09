# Maybe more optimized if I place an obtacle in the path of the guard in part 1
# and check if the guard is in a loop by checking of he hits an obstacle in the same direction more than once

def turn_right(dir: tuple[int, int]) -> tuple[int, int]:
    if (dir == (-1, 0)):
        return (0, 1)
    elif (dir == (0, 1)):
        return (1, 0)
    elif (dir == (1, 0)):
        return (0, -1)
    elif (dir == (0, -1)):
        return (-1, 0)
    else:
        return (0, 0)

def change_character(content, i: int, j: int, dir: tuple):
    if content[i][j] == '^':
        return
    if content[i][j] == '.':
        content[i][j] = '1'
    else:
        content[i][j] = str(int(content[i][j]) + 1)

def is_guard_in_loop(content: list[str], i: int, j: int, dir: tuple[int, int]) -> bool:
    while (i > 0 and j > 0 and i < len(content) - 1 and j < len(content[i]) - 1):
        if (content[i + dir[0]][j + dir[1]] == '#'):
            dir = turn_right(dir)
            continue
        change_character(content, i, j, dir)
        i += dir[0]
        j += dir[1]
        if content[i][j] == '4':
            return True
    return False

def clear_maze(content: list[str]) -> list[str]:
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] != '^' and content[i][j] != '#':
                content[i][j] = '.'
    return content

def add_obtsacle(content: list[str], guard_i: int, guard_j: int) -> int:
    total = 0
    content = [list(line) for line in content]
    for i in range(len(content)):
        for j in range(len(content[i])):
            char = content[i][j]
            if char == '^':
                continue
            content[i][j] = '#'
            if is_guard_in_loop(content, guard_i, guard_j, (-1, 0)):
                total += 1
            content = clear_maze(content)
            content[i][j] = char
    return total

def guard_trail(content: list[str], i: int, j: int, dir: tuple[int, int]) -> list[str]:
    content = [list(line) for line in content]
    while (i > 0 and j > 0 and i < len(content) - 1 and j < len(content[i]) - 1):
        if (content[i + dir[0]][j + dir[1]] == '#'):
            dir = turn_right(dir)
            continue
        content[i][j] = 'X'
        i += dir[0]
        j += dir[1]
    content[i][j] = 'X'
    return content

def count_guard_locations(content: list[str], i: int, j: int, dir: tuple[int, int]) -> int:
    total = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (content[i][j] == 'X'):
                total += 1
    return total

def find_guard(content: list[str]) -> tuple[int, int]:
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (content[i][j] == '^'):
                return i, j
    return -1, -1

def main() -> None:
    with open('input.txt', 'r') as file:
        original = file.readlines()
    original = [x.strip() for x in original]
    i, j = find_guard(original)
    content = guard_trail(original, i, j, (-1, 0))
    print(count_guard_locations(content, i, j, (-1, 0)))
    print(add_obtsacle(original, i, j))

if __name__ == "__main__":
    main()