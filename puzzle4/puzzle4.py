
def find_xmas(content: list[str], i:int, j:int, dir: tuple[int, int], tofind: str) -> bool:
    tofindindex = 0
    while (tofindindex < len(tofind)):
        if (i < 0 or j < 0 or i >= len(content) or j >= len(content[i]) or content[i][j] != tofind[tofindindex]):
            return False
        i += dir[0]
        j += dir[1]
        tofindindex += 1
    return True

def find_all_xmas(content: list[str]) -> int:
    total = 0
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (content[i][j] == 'X'):
                for dir in direction:
                    if (find_xmas(content, i, j, dir, "XMAS")):
                        total += 1
    return total

def find_mas_cross(content: list[str], i: int, j: int) -> bool:
    if ((find_xmas(content, i - 1, j + 1, (1, -1), "MAS") or find_xmas(content, i - 1, j + 1, (1, -1), "SAM"))
        and (find_xmas(content, i + 1, j + 1, (-1, -1), "MAS") or find_xmas(content, i + 1, j + 1, (-1, -1), "SAM"))):
        return True
    return False

def finf_all_mas_crosses(content: list[str]) -> int:
    total = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if (content[i][j] == 'A'):
                if (find_mas_cross(content, i, j)):
                    total += 1
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print(find_all_xmas(content))
    print(finf_all_mas_crosses(content))

if __name__ == "__main__":
    main()