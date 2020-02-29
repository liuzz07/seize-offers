#!/usr/bin/env python3
# coding: utf-8

"""
整数m变成整数n需要改变多少位
题目：输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n。
比如10的二进制位为1010，13的二进制位为1101，需要改变3位
"""


def number_of_change_bits(m: int, n: int) -> int:
    r = m ^ n
    count = number_of_1(r)
    return count


def number_of_1(n: int):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


if __name__ == "__main__":
    print(number_of_change_bits(10, 13))
    print(number_of_change_bits(8, 0))
    print(number_of_change_bits(7, 23))
    print(number_of_change_bits(15, 28))
    print(number_of_change_bits(234325, 135128))
