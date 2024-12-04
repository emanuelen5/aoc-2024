import bisect


def part1(lines):
    part1 = 0
    left_list = []
    right_list = []

    for line in lines:
        l, r = line.split()
        bisect.insort(left_list, int(l))
        bisect.insort(right_list, int(r))

    for l, r in zip(left_list, right_list):
        distance = abs(l - r)
        part1 += distance
    return part1
