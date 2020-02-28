#!/usr/bin/env python3
# coding: utf-8

"""
进制转换
题目：在Excel2003中，用A表示第1列，B表示第2列......Z表示第26列，
AA表示第27列，AB表示第28列......依次类推。请写出一个函数，输入
用字母表示的列号编码，输出它是第几列。
"""


def base_conversion(s: str) -> int:
    if not s or not s.isalpha():
        return "error:invalid input!"
    num = 0
    for index, value in enumerate(s[::-1]):
        num += (ord(value) - 64) * 26 ** index
    return num


if __name__ == "__main__":
    print(base_conversion("A"))
    print(base_conversion("M"))
    print(base_conversion("Z"))
    print(base_conversion("AA"))
    print(base_conversion("AM"))
    print(base_conversion("BB"))
    print(base_conversion("AAA"))
    print(base_conversion(""))
