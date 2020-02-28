#!/usr/bin/env python3
# coding: utf-8

"""
面试题之八：旋转数组的最小数字
题目：把一个数组最开始的若干个元素半岛数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组[3,4,5,1,2]
为[1,2,3,4,5]的一个旋转，该数组的最小值为1
"""

from typing import List


def min_num_in_rotated_array(numbers: List[int]) -> int:
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    if numbers[-1] > numbers[0]:
        return numbers[0]

    start, end = 0, len(numbers) - 1
    while start < end:
        mid = (start + end) // 2

        if numbers[mid] > numbers[end]:
            start = mid + 1
        elif numbers[mid] < numbers[end]:
            end = mid
        else:
            end -= 1
    return numbers[end]


if __name__ == "__main__":
    l1 = [3, 4, 5, 1, 2]
    print(min_num_in_rotated_array(l1))

    l2 = [5, 6, 2]
    print(min_num_in_rotated_array(l2))

    l3 = [10, 3]
    print(min_num_in_rotated_array(l3))

    l4 = [2, 3, 4, 5, 6, 7, -1]
    print(min_num_in_rotated_array(l4))

    l5 = [3, 4, 5, 6, 7, 0, 2]
    print(min_num_in_rotated_array(l5))

    l6 = [5, -2, 2, 3, 4]
    print(min_num_in_rotated_array(l6))

    l7 = [5, 6, -3, 2, 3, 4]
    print(min_num_in_rotated_array(l7))

    l8 = [5, 6, 7, 8, 1, 2, 3, 4]
    print(min_num_in_rotated_array(l8))

    l9 = [9, 10, 11, 12, 1, 2, 3, 4, 5]
    print(min_num_in_rotated_array(l9))

    l10 = [3]
    print(min_num_in_rotated_array(l10))

    l11 = [2, 2, 2, 0, 1]
    print(min_num_in_rotated_array(l11))

    l12 = []
    print(min_num_in_rotated_array(l12))
