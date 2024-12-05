
# Read the file and split it into two parts
def read_file_parts(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
    part1 = []
    part2 = []
    is_part2 = False
    for line in lines:
        line = line.strip()
        if ',' in line:
            is_part2 = True
        if is_part2:
            part2.append(line)
        else:
            part1.append(line)
    return part1, part2

# PART 1
def get_rule_dictionary(rules: list[str]) -> dict[int, list[int]]:
    rule_dict = {}
    for rule in rules:
        if rule == '':
            continue
        rule = rule.split('|')
        page1 = int(rule[0])
        page2 = int(rule[1])
        if (page2 not in rule_dict):
            rule_dict[page2] = []
        rule_dict[page2].append(page1)
    return rule_dict

def is_breaking_rule(rule_dict: dict, manual: list[int]) -> bool:
    for i in range(len(manual)):
        for j in range(i + 1, len(manual)):
            if manual[i] in rule_dict:
                for page in rule_dict[manual[i]]:
                    if page == manual[j]:
                        return True
    return False

def check_rule(rule_dict: dict, manuals: list[str]) -> int:
    total = 0
    for manual in manuals:
        manual = manual.split(',')
        manual = [int(x) for x in manual]
        if (is_breaking_rule(rule_dict, manual)):
            continue
        total += manual[len(manual) // 2]
    return total

# PART 2
def get_incorrect_manuals(rule_dict: dict, manuals: list[str]) -> list[list[int]]:
    incorrect_manuals = []
    for manual in manuals:
        manual = manual.split(',')
        manual = [int(x) for x in manual]
        if (is_breaking_rule(rule_dict, manual)):
            incorrect_manuals.append(manual)
    return incorrect_manuals

def order_manual(rule_dict: dict, manual: list[int]) -> None:
    for i in range(len(manual)):
        for j in range(i + 1, len(manual)):
            if manual[i] in rule_dict:
                for page in rule_dict[manual[i]]:
                    if page == manual[j]:
                        manual[i], manual[j] = manual[j], manual[i]

def order_incorrect_manuals(rule_dict: dict, incorrect_manuals: list[list[int]]) -> int:
    total = 0
    for manual in incorrect_manuals:
        order_manual(rule_dict, manual)
        total += manual[len(manual) // 2]
    return total

def main() -> None:
    rules, manuals = read_file_parts("input.txt")
    rule_dict = get_rule_dictionary(rules)
    print(check_rule(rule_dict, manuals))
    incorrect_manuals = get_incorrect_manuals(rule_dict, manuals)
    print(order_incorrect_manuals(rule_dict, incorrect_manuals))

if __name__ == "__main__":
    main()