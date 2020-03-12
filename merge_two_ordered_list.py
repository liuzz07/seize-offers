#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十七：合并两个有序的链表
题目：输入两个递增排序的链表，合并这两个链表并使新链表中结点仍然是按照递增排序的。
"""


class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def merge_two_ordered_list(head1: ListNode, head2: ListNode) -> ListNode:
    """递归"""
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val < head2.val:
        head1.next = merge_two_ordered_list(head1.next, head2)
        return head1
    else:
        head2.next = merge_two_ordered_list(head1, head2.next)
        return head2


def merge_two_ordered_list_v2(head1: ListNode, head2: ListNode) -> ListNode:
    """循环"""
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    dummyhead = ListNode(0)
    cur = dummyhead
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            cur.next = head1        # cur指向head1
            cur = cur.next          # cur移动到head1(已经确定head1是当前最小的)
            head1 = head1.next      # head1后移一步
        else:
            cur.next = head2
            cur = cur.next
            head2 = head2.next

    if head1 is None:
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
    node2 = ListNode(3)
    node3 = ListNode(7)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(3)
    node6 = ListNode(3)
    node7 = ListNode(6)
    node8 = ListNode(9)
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node = merge_two_ordered_list_v2(node1, node4)
    travel(node)
    print("==================================")

    node9 = ListNode(-1)
    node10 = ListNode(0)
    node = merge_two_ordered_list(node10, node9)
    travel(node)
    print("==================================")

    node11 = ListNode(2)
    node = merge_two_ordered_list_v2(node11, None)
    travel(node)
    print("==================================")

    node = merge_two_ordered_list_v2(None, None)
    travel(node)
