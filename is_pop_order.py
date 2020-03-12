#!/usr/bin/env python3
# coding: utf-8

"""
面试题之二十二：栈的压入、弹出序列
题目：输入两个整数序列。第一个表示栈的压入顺序，请判断第二个是否是栈的弹出顺序。
假设压入的数字均不相等

示例：
输入
    压入序列：[1, 2, 3, 4, 5]
    弹出序列：[4, 5, 3, 2, 1]

输出
    True

思路：使用辅助栈
1) 遍历pushed中的元素
2) 当j<len(popped)且栈顶元素等于popped[j]时弹出栈顶元素，j加1
3) 遍历结束时，如果栈为空，则返回True,否则返回False
"""

from typing import List


def is_pop_order(pushed: List[int], popped: List) -> bool:
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return not stack


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 5, 3, 2, 1]
    print(is_pop_order(nums1, nums2))

    nums1 = [1, 2, 3, 4, 6, 5]
    nums2 = [4, 5, 6, 3, 2, 1]
    print(is_pop_order(nums1, nums2))

    nums3 = [4, 3, 5, 1, 2]
    print(is_pop_order(nums1, nums3))

    nums4 = [1, 2]
    nums5 = [1, 2]
    nums6 = [2, 1]
    print(is_pop_order(nums4, nums5))
    print(is_pop_order(nums4, nums6))

    nums7 = [3, 4, 5]
    nums8 = [3, 4, 5]
    nums9 = [4, 3, 5]
    print(is_pop_order(nums7, nums8))
    print(is_pop_order(nums7, nums9))

    nums10 = [2]
    nums11 = [2]
    nums12 = [3]
    print(is_pop_order(nums10, nums11))
    print(is_pop_order(nums10, nums12))

    nums13 = []
    nums14 = []
    print(is_pop_order(nums13, nums14))
