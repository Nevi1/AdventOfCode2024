import re

def find_mul(content: str) -> int:
    total = 0
    ignored = False
    found = re.finditer("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)|do\\(\\)|don't\\(\\)", content)
    for match in found:
        if match.group(0) and match.group(2) and not ignored:
            a, b = match.groups()
            total += int(a) * int(b)
        elif match.group(0) == "do()":
            ignored = False
        elif match.group(0) == "don't()":
            ignored = True
    return total

def main():
    file = open("input.txt", "r")
    content = file.read()
    print(find_mul(content))
    file.close()

if __name__ == "__main__":
    main()