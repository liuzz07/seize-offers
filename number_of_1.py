#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十：二进制中1的个数
题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。
例如把9表示成二级制是1001，有2位是1。因此如果输入9，该函数输出2。
"""


def number_of_1(n: int) -> int:
    count = 0
    flag = 1
    while abs(flag) <= abs(n):
        if n & flag:
            count += 1
        flag = flag << 1

    return count


def number_of_1_v2(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1)
        count += 1

    return count


if __name__ == "__main__":
    print(number_of_1(0))  # 0
    print(number_of_1(1))  # 1
    print(number_of_1(2))  # 10
    print(number_of_1(5))  # 101
    print(number_of_1(9))  # 1001
    print(number_of_1(10))  # 1010
    print(number_of_1(18))  # 10010
    print(number_of_1(888))  # 1101111000
    print(number_of_1(999999999))  # 111011100110101100100111111111

    print(number_of_1(-1))
    print(number_of_1(-10))
    print(number_of_1(-23))

    print(number_of_1_v2(0))
    print(number_of_1_v2(1))
    print(number_of_1_v2(7))
    print(number_of_1_v2(119))
