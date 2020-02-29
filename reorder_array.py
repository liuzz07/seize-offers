#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十四：调整数组顺寻使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
"""

from typing import List


def reorder_array(arr: List[int]) -> None:
    """v1版本，时间复杂度O(n2)"""
    i, count = 0, 0
    while count < len(arr) and i < len(arr):
        if not (arr[i] & 1):
            arr.append(arr.pop(i))
            count += 1
        else:
            i += 1


def reorder_array_v2(arr: List[int]) -> None:
    """v2版本，时间复杂度O(n)"""
    i, j = 0, len(arr) - 1
    while i < j:
        if not (arr[i] & 1) and (arr[j] & 1):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] & 1:
            i += 1
        elif not(arr[j] & 1):
            j -= 1


if __name__ == "__main__":
    arr1 = [5, 2, 4, 2, 3, 5]
    reorder_array_v2(arr1)
    print(arr1)

    arr2 = [3, 1, 1, 4, 8, 6]
    reorder_array_v2(arr2)
    print(arr2)

    arr3 = [2, 10, 12, 3, 9, 11]
    reorder_array_v2(arr3)
    print(arr3)

    arr4 = [1, 3, 3, 3, 5]
    reorder_array_v2(arr4)
    print(arr4)

    arr5 = [8, 8, 8, 8, 8]
    reorder_array_v2(arr5)
    print(arr5)

    arr6 = [1, 8]
    reorder_array_v2(arr6)
    print(arr6)

    arr7 = [8, 1]
    reorder_array_v2(arr7)
    print(arr7)

    arr8 = [3]
    reorder_array_v2(arr8)
    print(arr8)

    arr9 = [6]
    reorder_array_v2(arr9)
    print(arr9)

    arr10 = []
    reorder_array_v2(arr10)
    print(arr10)

    arr11 = [-2, 0, -1, 3, -6]
    reorder_array_v2(arr11)
    print(arr11)
