#!/usr/bin/env python3
# coding: utf-8

"""
面试题之二十五：二叉树中和为某一值的路径
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径，
从根结点开始往下一直到叶子结点所经过的结点形成一条路径

示例：
输入一下二叉树和sum=8
        5
       / \
      3   6
     /   / \
    1   2   1
     \
      4

输出
    [
        [5, 3],
        [3, 1, 4],
        [6, 2]
    ]

思路：
"""

from typing import List


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_in_tree(root: TreeNode, sum_num: int) -> List[List[int]]:
    res, path = [], []

    def helper(root, sum_num):
        if not root:
            return
        path.append(root.val)
        sum_num -= root.val
        print("root: ", root.val)
        print("path: ", path)
        print("sum: ", sum_num)
        print()
        # 如果是叶子结点并且结点的和等于输入的值，就打印路径
        if not root.left and not root.right and not sum_num:
            res.append(path[:])
        helper(root.left, sum_num)
        helper(root.right, sum_num)
        path.pop()

    helper(root, sum_num)
    return res


if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node4.right = node6
    node3.right = node7
    print(path_in_tree(node1, 9))
    print(path_in_tree(node1, 12))
    print(path_in_tree(node1, 13))
