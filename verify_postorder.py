#!/usr/bin/env python3
# coding: utf-8

"""
面试题之二十四：二叉搜索数的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果
如果是返回True，否则返回False。假设输入的数组任意两个数字都不相同
"""

from typing import List


def verify_postorder(postorder: List[int]) -> bool:
    if not postorder or len(postorder) == 1:
        return True

    i = 0
    left = []
    while i < len(postorder) - 1 and postorder[i] < postorder[-1]:
        left.append(postorder[i])
        i += 1
    right = postorder[i: -1]
    for item in right:
        if item <= postorder[-1]:
            return False

    return verify_postorder(left) and verify_postorder(right)


if __name__ == "__main__":
    postorder = [5, 7, 6, 9, 11, 10, 8]
    print(verify_postorder(postorder))

    postorder = [7, 4, 6, 5]
    print(verify_postorder(postorder))

    postorder = [3, 5, 6, 9]
    print(verify_postorder(postorder))

    postorder = [9, 8, 7, 6]
    print(verify_postorder(postorder))

    postorder = [7, 8, 6, 5]
    print(verify_postorder(postorder))

    postorder = [7, 6, 8, 5]
    print(verify_postorder(postorder))

    postorder = [1, 3, 2, 6, 5]
    print(verify_postorder(postorder))

    postorder = [18, 10, 12, 9, 7, 8, 11]
    print(verify_postorder(postorder))

    postorder = []
    print(verify_postorder(postorder))
