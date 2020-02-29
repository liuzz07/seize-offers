#!/usr/bin/env python3
# coding: utf-8

"""
测试位运算&与取余运算%的效率高低
"""

import time


def time_test(n: int) -> None:
    start_time = time.time()
    for i in range(n):
        a = 123456789 & 1
    end_time = time.time()
    print("位运算时间：", end_time - start_time)

    start_time = time.time()
    for i in range(n):
        b = 123456789 % 2
    end_time = time.time()
    print("取余运算时间：", end_time - start_time)


if __name__ == "__main__":
    time_test(1000000000)
