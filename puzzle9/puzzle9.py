
def arrange_diskmap(diskmap: str) -> str:
    num = 0
    id = 0
    is_free_space = False
    arranged_disk = []
    for number in diskmap:
        num = int(number)
        if not is_free_space:
            for i in range(num):
                arranged_disk.append(id)
            id += 1
        else:
            for i in range(num):
                arranged_disk.append('.')
        is_free_space = not is_free_space
    return arranged_disk

def compact_diskmap(diskmap: list) -> str:
    index = 0
    from_end_index = len(diskmap) - 1
    while index < from_end_index:
        while diskmap[index] != '.':
            index += 1
        while diskmap[from_end_index] == '.':
            from_end_index -= 1
        if index <= from_end_index:
            diskmap[index], diskmap[from_end_index] = diskmap[from_end_index], diskmap[index]
        index += 1
        from_end_index -= 1
    return diskmap

def get_chunk_len(diskmap: list, index: int, tocheck, right: bool) -> int:
    length = 0
    tmp = index
    while tmp >= 0 and tmp < len(diskmap) and diskmap[tmp] == tocheck:
        tmp += 1 if right else -1
        length += 1
    return length

def compact_diskmap_chunk(diskmap: list) -> str:
    index = 0
    from_end_index = len(diskmap) - 1
    while index < from_end_index:
        while diskmap[index] != '.':
            index += 1
        while diskmap[from_end_index] == '.':
            from_end_index -= 1
        free_space_len = get_chunk_len(diskmap, index, '.', True)
        disk_len = get_chunk_len(diskmap, from_end_index, diskmap[from_end_index], False)
        if free_space_len >= disk_len and index < from_end_index:
            while disk_len > 0:
                diskmap[index], diskmap[from_end_index] = diskmap[from_end_index], diskmap[index]
                index += 1
                from_end_index -= 1
                disk_len -= 1
        elif index + disk_len < from_end_index:
            index += free_space_len
            continue
        index = 0
        from_end_index -= disk_len
    return diskmap

def get_checksum(diskmap: list) -> int:
    checksum = 0
    for i in range(len(diskmap)):
        if diskmap[i] == '.':
            continue
        checksum += i * diskmap[i]
    return checksum

def main() -> None:
    with open('input.txt', 'r') as file:
        input = file.readlines()
    input = input[0].strip()
    print(get_checksum(compact_diskmap(arrange_diskmap(input))))
    print(get_checksum(compact_diskmap_chunk(arrange_diskmap(input))))


if __name__ == "__main__":
    main()