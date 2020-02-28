#!/usr/bin/env python3
# coding: utf-8

"""
面试题之九：斐波那契数列
"""


def fibnacci(n: int) -> int:
    if n <= 2:
        return 1
    f1 = f2 = 1
    for i in range(1, n - 1):
        f1, f2 = f2, f1 + f2
    return f2


if __name__ == "__main__":
    print(fibnacci(1))
    print(fibnacci(2))
    print(fibnacci(3))
    print(fibnacci(4))
    print(fibnacci(5))
