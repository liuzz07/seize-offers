#!/usr/bin/env python3
# coding: utf-8

'''
面试题之五：从尾到头打印链表
'''


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def print_list_node_reversingly(head: ListNode) -> None:
    stack = []
    p = head
    while p is not None:
        stack.append(p.val)
        p = p.next
    while len(stack) != 0:
        print(stack.pop())


if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    print_list_node_reversingly(p1)

    p1 = ListNode(1)
    print_list_node_reversingly(p1)

    p = None
    print_list_node_reversingly(p)
