#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十一：数字的整数次方
题目：实现函数double Power(double base, int exponent)，
求base的exponent次方，不得使用库函数
"""


def my_power(base: float, exponent: int) -> float:
    if type(exponent) != int:
        return "error: invalid input!"
    if base == 0 and exponent < 0:
        return "error: invalid input!"
    if exponent == 0:
        return 1.0
    elif exponent > 0:
        result = 1.0
        while exponent:
            result *= base
            exponent -= 1
    else:
        ex = -exponent
        result = 1.0
        while ex:
            result *= base
            ex -= 1
        result = 1.0 / result

    return result


if __name__ == "__main__":
    print(my_power(2.5, 3))
    print(my_power(5.345, 4))
    print(my_power(3.201, 1))
    print(my_power(5.678, 0))
    print(my_power(0.678, 6))
    print(my_power(10.954, -1))
    print(my_power(6.9, -2))
    print(my_power(-7.123, 5))
    print(my_power(-1.679, -5))
    print(my_power(0, 5))
    print(my_power(0.0, -2))
    print(my_power(2.5, "a"))
