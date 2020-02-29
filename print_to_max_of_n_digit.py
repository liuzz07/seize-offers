#!/usr/bin/env python3
# coding: utf-8

"""
打印1到最大的n位数
"""


def print_to_max_n_digit(n: int):
    num = 1
    for i in range(n):
        num *= 10

    for i in range(1, num):
        print(i)


if __name__ == "__main__":
    print_to_max_n_digit(3)
    print_to_max_n_digit(5)
    print_to_max_n_digit(8)
