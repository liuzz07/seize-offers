#!/usr/bin/env python3
# coding: utf-8

"""
补充：合并k个有序链表
题目：合并 k 个排序链表，返回合并后的排序链表
"""

from typing import List


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def merge_k_ordered_list(lists: List[ListNode]) -> ListNode:
    if not lists:
        return
    head = lists[0]
    i = 1
    while i < len(lists):
        head = merge_two_ordered_list(head, lists[i])
        i += 1

    return head


def merge_two_ordered_list(head1: ListNode, head2: ListNode) -> ListNode:
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    dummyhead = ListNode(0)
    cur = dummyhead
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            cur.next = head1
            cur = cur.next
            head1 = head1.next
        else:
            cur.next = head2
            cur = cur.next
            head2 = head2.next

    if head1 is None:       # 处理最后一个结点的指向
        cur.next = head2
    else:
        cur.next = head1

    return dummyhead.next


def travel(head: ListNode) -> None:
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(3)
    node6 = ListNode(3)
    node7 = ListNode(8)
    node4.next = node5
    node5.next = node6
    node6.next = node7

    node8 = ListNode(0)
    node9 = ListNode(1)
    node10 = ListNode(9)
    node8.next = node9
    node9.next = node10

    lists = [node1, node4, node8]
    node = merge_k_ordered_list(lists)
    travel(node)
    print("=========================")

    node10 = ListNode(10)
    node11 = ListNode(11)
    lists = [None, node10, node11]
    node = merge_k_ordered_list(lists)
    travel(node)
    print("=========================")

    node12 = ListNode(12)
    lists = [node12]
    node = merge_k_ordered_list(lists)
    travel(node)
    print("=========================")

    node = merge_k_ordered_list([])
    travel(node)
