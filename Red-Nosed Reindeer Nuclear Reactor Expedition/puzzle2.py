def check_sorted_descending(list: list[int], permited: int) -> bool:
    bad_count = 0
    for i in range(len(list) - 1):
        if list[i] < list[i + 1] or (abs(list[i] - list[i + 1]) > 3 or abs(list[i] - list[i + 1]) < 1):
            bad_count += 1
        if bad_count > permited:
            return False
    return True

def check_sorted_ascending(list: list[int], permited: int) -> bool:
    bad_count = 0
    for i in range(len(list) - 1):
        if list[i] > list[i + 1] or (abs(list[i] - list[i + 1]) > 3 or abs(list[i] - list[i + 1]) < 1):
            bad_count += 1
        if bad_count > permited:
            return False
    return True

def content_loop(content : str) -> int:
    total = 0
    for line in content.split("\n"):
        list = []
        split = line.split(" ")
        if len(split) < 2:
            break
        for i in range(len(split)):
            list.append(int(split[i]))
        if (check_sorted_ascending(list, 1) or check_sorted_descending(list, 1)):
            total += 1
    return total

def main():
    file = open("input.txt", "r")
    content = file.read()
    print(content_loop(content))

if __name__ == "__main__":
    main()