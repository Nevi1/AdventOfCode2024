from itertools import combinations

def get_antennas_pairs_positions(input: list[str], char) -> list[tuple]:
    positions = []
    for row_idx, line in enumerate(input):
        for col_idx, ch in enumerate(line):
            if ch == char:
                positions.append((row_idx, col_idx))
    pairs = list(combinations(positions, 2))
    return pairs

def add_antinodes(antenna_dict: dict, input: list[str]) -> int:
    distance = (0, 0)
    antinode_pos1 = (0, 0)
    antinode_pos2 = (0, 0)
    antinodes_positions = []
    for (key, value) in antenna_dict.items():
        for pair in value:
            distance = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            antinode_pos1 = (pair[0][0] - distance[0], pair[0][1] - distance[1])
            antinode_pos2 = (pair[1][0] + distance[0], pair[1][1] + distance[1])
            if pair[0] not in antinodes_positions:
                antinodes_positions.append(pair[0])
            if pair[1] not in antinodes_positions:
                antinodes_positions.append(pair[1])
            while antinode_pos1[0] >= 0 and antinode_pos1[1] >= 0 and antinode_pos1[0] < len(input) and antinode_pos1[1] < len(input[0]):
                if antinode_pos1 not in antinodes_positions:
                    antinodes_positions.append(antinode_pos1)
                antinode_pos1 = (antinode_pos1[0] - distance[0], antinode_pos1[1] - distance[1])
            while antinode_pos2[0] >= 0 and antinode_pos2[1] >= 0 and antinode_pos2[0] < len(input) and antinode_pos2[1] < len(input[0]):
                if antinode_pos2 not in antinodes_positions:
                    antinodes_positions.append(antinode_pos2)
                antinode_pos2 = (antinode_pos2[0] + distance[0], antinode_pos2[1] + distance[1])
    return len(antinodes_positions)

def main() -> None:
    with open('input.txt', 'r') as file:
        input = file.readlines()
    input = [x.strip() for x in input]
    antenna_dict = {}
    for line in input:
        for ch in line:
            if antenna_dict.get(ch) == None and ch != '.':
                antenna_dict[ch] = get_antennas_pairs_positions(input, ch)
    print(add_antinodes(antenna_dict, input))

if __name__ == "__main__":
    main()