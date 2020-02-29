#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十六：反转链表
题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    if head is None:
        return head
    if head.next is None:
        return head

    pre = head
    cur = head.next
    while cur.next is not None:
        p = cur.next
        cur.next = pre
        pre = cur
        cur = p
    cur.next = pre
    head.next = None

    return cur


def travel(p: ListNode) -> None:
    while p is not None:
        print(p.val)
        p = p.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node = reverse_list(node1)
    travel(node)

    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node = reverse_list(node1)
    travel(node)

    node = reverse_list(None)
    travel(node)
