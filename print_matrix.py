#!/usr/bin/env python3
# coding: utf-8

"""
面试题之二十：顺时针打印矩阵
题目：输入一个矩阵，按照由外向里以顺时针的顺序依次打印出每一个数字。

示例：
输入
    1   2   3   4

    5   6   7   8

    9   10  11  12

    13  14  15  16

输出
    1、2、3、4、5、6、7、8、9、10、11、12、13、14、15、16

"""

from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    # 处理边界条件(已在后续代码里实现，故舍去)
    #if len(matrix) == 1:
    #    for item in matrix[0]:
    #        print(item)
    #    return
    #if len(matrix[0]) == 1:
    #    for item in matrix:
    #        print(item[0])
    #    return

    i, j = 0, 0
    k, l = len(matrix) - 1, len(matrix[0]) - 1
    while i <= k and j <= l:
        print_circle(matrix, i, j, k, l)
        i += 1
        j += 1
        k -= 1
        l -= 1


def print_circle(matrix, i, j, k, l):
    """打印矩阵的一圈"""
    # 左上 --> 右上
    m, n = i, j
    while n <= l:
        print(matrix[m][n])
        n += 1
    # 右上 --> 右下
    m, n = i + 1, l
    while m <= k:
        print(matrix[m][n])
        m += 1
    # 右下 --> 左下
    m, n = k, l - 1
    while n >= j and m > i:     # m>i用于处理单行的情形，避免重复打印
        print(matrix[m][n])
        n -= 1
    # 左下 --> 左上
    m, n = k - 1, j
    while m >= i + 1 and n < l:  # n<l用于处理单列的情形，避免重复打印
        print(matrix[m][n])
        m -= 1


if __name__ == "__main__":
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print_matrix(matrix1)

    matrix2 = [[1, 2, 3, 4]]
    print_matrix(matrix2)

    matrix3 = [[1], [2], [3], [4]]
    print_matrix(matrix3)

    matrix4 = [[1, 2, 3], [5, 6, 7]]
    print_matrix(matrix4)

    matrix5 = [[1, 2], [3, 4]]
    print_matrix(matrix5)

    matrix6 = [[1]]
    print_matrix(matrix6)

    matrix7 = [[]]
    print_matrix(matrix7)

    matrix8 = []
    print_matrix(matrix8)
