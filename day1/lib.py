import bisect
import collections


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


def part2(lines):
    res = 0
    left_list = []
    right_list = []

    for line in lines:
        l, r = line.split()
        bisect.insort(left_list, int(l))
        bisect.insort(right_list, int(r))

    right_counts = collections.Counter(right_list)

    for l in left_list:
        right_count = right_counts.get(l, 0)
        sim_score = l * right_count
        res += sim_score

    return res
