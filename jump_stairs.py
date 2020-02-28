#!/usr/bin/env python3
# coding: utf-8

"""
补充：跳台阶
题目：一只青蛙一次可以跳上一级台阶，也可以跳上两级台阶。
求该青蛙跳上一个级台阶总共有多少种跳法
"""


def jump_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    s1, s2 = 1, 2
    for i in range(1, n - 1):
        s1, s2 = s2, s1 + s2
    return s2


if __name__ == "__main__":
    print(jump_stairs(1))
    print(jump_stairs(2))
    print(jump_stairs(3))
    print(jump_stairs(4))
    print(jump_stairs(5))
    print(jump_stairs(100))
