#!/usr/bin/env python3
# coding: utf-8

"""
求链表的中间结点
题目：如果链表中结点总数为奇数，返回中间结点；如果结点总数是偶数，
返回中间两个结点的任意一个。
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def find_mid_node(p: ListNode) -> ListNode:
    fast, slow = p, p
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


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

    print(find_mid_node(node1).val)

    node6 = ListNode(6)
    node5.next = node6
    print(find_mid_node(node1).val)

    node7 = ListNode(7)
    node8 = ListNode(8)
    node7.next = node8
    print(find_mid_node(node7).val)

    node9 = ListNode(9)
    print(find_mid_node(node9).val)
