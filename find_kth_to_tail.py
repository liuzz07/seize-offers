#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十五：链表中倒数第k个结点
题目：输入一个链表，输出该链表中倒数第k个结点，为了符合大多人的习惯，
从1开始计数，即尾结点为倒数第1个结点
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def find_kth_to_tail(p: ListNode, k: int) -> ListNode:
    if k <= 0:
        return "error: invalid input!"
    p1, p2 = p, p
    count = 0
    while p1 and p1.next is not None:
        p1 = p1.next
        count += 1
        if count >= k:
            p2 = p2.next
    if p2 is p and k > (count + 1):
        return "error: invalid input!"
    return p2


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node = find_kth_to_tail(node1, 3)
    try:
        print(node.val)
    except Exception:
        print(node)

    node = find_kth_to_tail(node1, 5)
    try:
        print(node.val)
    except Exception:
        print(node)

    node = find_kth_to_tail(node1, 0)
    try:
        print(node.val)
    except Exception:
        print(node)

    node = find_kth_to_tail(node1, 7)
    try:
        print(node.val)
    except Exception:
        print(node)

    node = find_kth_to_tail(None, 2)
    try:
        print(node.val)
    except Exception:
        print(node)

    node6 = ListNode(6)
    node = find_kth_to_tail(node6, 1)
    try:
        print(node.val)
    except Exception:
        print(node)

    node = find_kth_to_tail(node6, 2)
    try:
        print(node.val)
    except Exception:
        print(node)
