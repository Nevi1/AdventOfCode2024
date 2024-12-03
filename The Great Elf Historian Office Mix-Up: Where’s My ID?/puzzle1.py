# sort() is for cowards
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def parse_input(content: str) -> tuple[list[str], list[str]]:
    list1 = []
    list2 = []
    for line in content.split("\n"):
        split = line.split("   ") # I don't care if it only works with the input, who needs error handling
        if (len(split) < 2):
            break
        list1.append(split[0])
        list2.append(split[1])
    return list1, list2

def add_distance(list1: list[str], list2: list[str]) -> int:
    total = 0
    for i in range(len(list1)):
        total += abs(int(list1[i]) - int(list2[i]))
    return total

def get_iterations_map(list: list[str]) -> dict:
    iterations = {}
    for i in range(len(list)):
        if list[i] in iterations:
            iterations[list[i]] += 1
        else:
            iterations[list[i]] = 1
    return iterations

def get_similarity_score(itMap: dict, tofind: list[str]) -> int:
    score = 0
    for i in range(len(tofind)):
        if tofind[i] in itMap:
            score += int(tofind[i]) * itMap[tofind[i]]
    return score

def main() -> None:
    file = open("input.txt", "r")
    content = file.read()
    list1, list2 = parse_input(content)
    list1 = quick_sort(list1)
    list2 = quick_sort(list2)
    print(add_distance(list1, list2))
    iterations_map = get_iterations_map(list1)
    print(get_similarity_score(iterations_map, list2))

if __name__ == "__main__":
    main()