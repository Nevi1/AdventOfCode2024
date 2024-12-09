#Maybe ook into a DFS solution for this puzzle

from itertools import product

def get_parts(input: str) -> tuple:
    value = []
    equations = []
    for line in input:
        parts = line.split(':')
        value.append(parts[0].strip())
        equation = parts[1].strip().split(' ')
        equations.append(equation)
    return value, equations

def combine_value(left: int, right: int) -> int:
    rightlen = len(str(right))
    return left * (10 ** rightlen) + right

def can_attain_value(value: int, equation: list) -> bool:
    numbers = list(map(int, equation))
    operators = list(product(['+', '*', '|'], repeat=len(numbers)-1))

    for ops in operators:
        result = numbers[0]
        for num, op in zip(numbers[1:], ops):
            if op == '+':
                result += num
            elif op == '*':
                result *= num
            elif op == '|':
                result = combine_value(result, num)
        if result == value:
            return True
    return False

def main() -> None:
    with open('input.txt', 'r') as file:
        original = file.readlines()
    value, equations = get_parts(original)
    total = 0
    for val, eq in zip(value, equations):
        if can_attain_value(int(val), eq):
            total += int(val)
    print(total)

if __name__ == "__main__":
    main()