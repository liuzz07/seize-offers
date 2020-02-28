#!/usr/bin/env python3
# coding: utf-8

"""
给员工的年龄排序
题目：给员工年龄排序，要求时间效率为O(n)，可以使用O(n)的额外空间
"""

from typing import List


def age_sort(ages: List[int]) -> None:
    oldest_age = 99
    age_times = [0 for i in range(oldest_age + 1)]
    for age in ages:
        if age < 0 or age > oldest_age:
            return "errror:age out of range"
        age_times[age] += 1

    i = 0
    k = 0
    while i <= oldest_age:
        j = 0
        while j < age_times[i]:
            ages[k] = i
            k += 1
            j += 1
        i += 1


if __name__ == "__main__":
    import random
    ages = [random.randint(18, 99) for i in range(200)]
    age_sort(ages)
    print(ages)
