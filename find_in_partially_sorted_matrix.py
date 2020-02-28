#!/usr/bin/env python3
# coding:utf-8

'''
面试题之三：二维数组中的查找
'''

from typing import List


def find_in_partially_sorted_matrix(matrix: List[List[int]], num: int) -> bool:

    if not matrix or not matrix[0]:
        return False
    if num < matrix[0][0] or num > matrix[-1][-1]:
        return False

    i, j = len(matrix) - 1, 0
    while i >= 0 and j <= len(matrix[0]) - 1:
        if matrix[i][j] == num:
            return True
        elif matrix[i][j] < num:
            j += 1
        elif matrix[i][j] > num:
            i -= 1
    return False


if __name__ == '__main__':
    matrix = [
                [1, 2, 8, 9],
                [2, 4, 9, 12],
                [4, 7, 10, 13],
                [6, 8, 11, 15]
            ]
    #print(find_in_partially_sorted_matrix(matrix, 10))
    #print(find_in_partially_sorted_matrix(matrix, 4))
    #print(find_in_partially_sorted_matrix(matrix, 15))
    #print(find_in_partially_sorted_matrix(matrix, 9))
    #print(find_in_partially_sorted_matrix(matrix, 5))
    #print(find_in_partially_sorted_matrix(matrix, -1))
    #print(find_in_partially_sorted_matrix(matrix, 1))
    #print(find_in_partially_sorted_matrix(matrix, 18))

    matrix = [
            [-2, 1, 5, 9]
            ]
    #print(find_in_partially_sorted_matrix(matrix, -2))
    #print(find_in_partially_sorted_matrix(matrix, 5))
    #print(find_in_partially_sorted_matrix(matrix, 9))
    #print(find_in_partially_sorted_matrix(matrix, -1))
    #print(find_in_partially_sorted_matrix(matrix, -3))
    #print(find_in_partially_sorted_matrix(matrix, 10))

    matrix = [
            [-5,],
            [-2,],
            [3,],
            [6,],
            [8,]
            ]
    #print(find_in_partially_sorted_matrix(matrix, 0))
    #print(find_in_partially_sorted_matrix(matrix, -8))
    #print(find_in_partially_sorted_matrix(matrix, 6))
    #print(find_in_partially_sorted_matrix(matrix, 8))
    #print(find_in_partially_sorted_matrix(matrix, -5))
    #print(find_in_partially_sorted_matrix(matrix, 10))

    matrix = []
    #print(find_in_partially_sorted_matrix(matrix, 3))

    matrix = [
            [],
            [],
            []
            ]
    print(find_in_partially_sorted_matrix(matrix, 5))
