
def find_trailheads(map: list[list[int]]) -> list[tuple[int, int]]:
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(map: list[list[int]], x: int, y: int, prev_height: int) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == prev_height + 1

def dfs(map: list[list[int]], x: int, y: int, visited: set[tuple[int, int]]) -> set[tuple[int, int]]:
    if map[x][y] == 9:
        return {(x, y)}

    visited.add((x, y))
    reachable_nines = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(map, nx, ny, map[x][y]) and (nx, ny) not in visited:
            reachable_nines.update(dfs(map, nx, ny, visited))
    visited.remove((x, y))
    return reachable_nines

def calculate_score(map: list[list[int]], trailhead: tuple[int, int]) -> int:
    visited = set()
    return len(dfs(map, trailhead[0], trailhead[1], visited))

def dfs_count_paths(map: list[list[int]], x: int, y: int, visited: set[tuple[int, int]]) -> int:
    if map[x][y] == 9:
        return 1

    visited.add((x, y))
    path_count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(map, nx, ny, map[x][y]) and (nx, ny) not in visited:
            path_count += dfs_count_paths(map, nx, ny, visited)
    visited.remove((x, y))
    return path_count

def calculate_rating(map: list[list[int]], trailhead: tuple[int, int]) -> int:
    visited = set()
    return dfs_count_paths(map, trailhead[0], trailhead[1], visited)

def main() -> None:
    with open('input.txt', 'r') as file:
        input = file.readlines()
    input = [list(map(int, list(line.strip()))) for line in input]

    trailheads = find_trailheads(input)
    total_score = sum(calculate_score(input, trailhead) for trailhead in trailheads)
    rating = sum(calculate_rating(input, trailhead) for trailhead in trailheads)

    print(total_score)
    print(rating)

if __name__ == "__main__":
    main()