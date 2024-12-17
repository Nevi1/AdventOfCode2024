from collections import defaultdict

def apply_rules(num, lookup):
    if num in lookup:
        return lookup[num]
    if num == 0:
        lookup[num] = [1]
    elif len(str(num)) % 2 == 0:
        alpha = str(num)
        l = len(alpha) // 2
        alpha1, alpha2 = alpha[:l], alpha[l:]
        lookup[num] = [int(alpha1), int(alpha2)]
    else:
        lookup[num] = [num * 2024]
    return lookup[num]

def iterative_count_end_nodes(data, n):
    current_counts = defaultdict(int)
    for num in data:
        current_counts[num] += 1

    lookup = {}

    for iteration in range(n):
        next_counts = defaultdict(int)
        for num, count in current_counts.items():
            children = apply_rules(num, lookup)
            for child in children:
                next_counts[child] += count
        current_counts = next_counts

    total = sum(current_counts.values())
    return total

def main() -> None:
    with open('input.txt', 'r') as file:
        input = file.read().strip()
    stones = list(map(int, input.split(' ')))
    iterations = 75
    result = iterative_count_end_nodes(stones, iterations)
    print(result)

if __name__ == '__main__':
    main()