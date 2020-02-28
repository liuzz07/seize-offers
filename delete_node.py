#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十三：在O(1)的时间内删除链表结点
题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除结点。
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def delete_node(p_head: ListNode, p: ListNode):
    if p_head.next is None:
        p_head = None
        return
    if p.next is not None:
        p.val = p.next.val
        p.next = p.next.next
    else:
        p1 = p_head
        while p1.next != p:
            p1 = p1.next
        p1.next = None


def travel(p: ListNode) -> None:
    while p is not None:
        print(p.val)
        p = p.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    delete_node(node1, node4)
    travel(node1)
