
def flood_fill(x, y, plant_type, visited, input):
    stack = [(x, y)]
    area = 0
    perimeter = 0
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[0]):
                if input[nx][ny] == plant_type and (nx, ny) not in visited:
                    stack.append((nx, ny))
                elif input[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter

def turn_right(dir: tuple) -> tuple:
    if dir == (1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (1, 0)

def get_garden_sides(garden_pos: set) -> int:
    sides = set()
    dir = (1, 0)
    initial_pos = garden_pos[0]
    curr_pos = garden_pos[0]
    print(garden_pos)
    while True:
        if (curr_pos[0] + dir[0], curr_pos[1] + dir[1]) in garden_pos:
            curr_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])
        else:
            sides.add(curr_pos)
            dir = turn_right(dir)
            continue
        if curr_pos == initial_pos:
            break
    print(len(sides))
    return len(sides)

def flood_fill_sides(x, y, plant_type, visited, input):
    stack = [(x, y)]
    area = 0
    sides = 0
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[0]):
                if input[nx][ny] == plant_type and (nx, ny) not in visited:
                    stack.append((nx, ny))
                elif input[nx][ny] != plant_type:
                    sides += 1
            else:
                sides += 1
    return area, sides

def main() -> None:
    with open('test.txt', 'r') as file:
        input = file.readlines()
    input = [list(line.strip()) for line in input]

    visited = set()
    total_price = 0

    #Part 1
    for i in range(len(input)):
        for j in range(len(input[0])):
            if (i, j) not in visited:
                plant_type = input[i][j]
                area, perimeter = flood_fill(i, j, plant_type, visited, input)
                total_price += area * perimeter
    print(total_price)

    #Part 2
    visited = set()
    total_price = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if (x, y) not in visited:
                plant_type = input[x][y]
                area, sides = flood_fill_sides(x, y, plant_type, visited, input)
                total_price += area * sides
    print(total_price)

if __name__ == "__main__":
    main()