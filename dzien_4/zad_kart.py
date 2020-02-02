# def up_down(liczba):
#     return liczba - 1, liczba + 1
#
#
# def test_up_down():
#     assert up_down(5) == (4, 6)
# def consecutive(napis, sign):
#     count = 0
#     count1 = 0
#
#     for i in napis:
#
#         if i == sign:
#             count += 1
#             count1 = 0
#         else:
#             count1 = max(count, count1)
#             count = 0
#
#
#     return count1
import re


def consecutive(napis, sign):
    pattern = re.compile(f"{sign}")
    data = pattern.findall(napis)
    data = [len(x) for x in data]
    return data

def test_connection():
    assert consecutive("aaabbaabbbbaa","b") == 4
    # assert consecutive"aabbbbbaaaaaab") == 6
