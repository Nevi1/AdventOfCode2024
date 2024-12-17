import re

def get_machines(input):
    machines = []
    regex = re.compile(r'.*X\+(\d+), Y\+(\d+)')
    prize_regex = re.compile(r'.*X=(\d+), Y=(\d+)')

    for i in range(0, len(input), 3):
        button_a_match = regex.match(input[i])
        button_b_match = regex.match(input[i+1])
        prize_match = prize_regex.match(input[i+2])

        if button_a_match and button_b_match and prize_match:
            button_a = (int(button_a_match.group(1)), int(button_a_match.group(2)))
            button_b = (int(button_b_match.group(1)), int(button_b_match.group(2)))
            prize = (int(prize_match.group(1)) + 10000000000000, int(prize_match.group(2)) + 10000000000000)
            machines.append((button_a, button_b, prize))
    return machines

def resolve_system(button_a, button_b, prize) -> int:
    b, brem = divmod(button_a[1] * prize[0] - button_a[0] * prize[1], button_a[1] * button_b[0] - button_a[0] * button_b[1])
    a, arem = divmod(prize[0] - b * button_b[0], button_a[0])
    if arem != 0 or brem != 0:
        return 0
    return a * 3 + b

def main() -> None:
    with open('input.txt', 'r') as file:
        input = file.readlines()
    input = [x.strip() for x in input if x.strip()]

    machines = get_machines(input)
    total_tokens = 0

    for button_a, button_b, prize in machines:
        tokens = resolve_system(button_a, button_b, prize)
        total_tokens += tokens

    print(total_tokens)


if __name__ == "__main__":
    main()