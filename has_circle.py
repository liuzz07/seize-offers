#!/usr/bin/env python3
# coding: utf-8

"""
判断链表是否有环
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def has_circle(p: ListNode) -> bool:
    fast, slow = p, p
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(has_circle(node1))

    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node5.next = node6
    node6.next = node7
    print(has_circle(node5))

    node8 = ListNode(8)
    print(has_circle(node8))

    print(has_circle(None))
