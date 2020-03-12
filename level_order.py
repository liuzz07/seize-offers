#!/usr/bin/env python3
# coding: utf-8

"""
面试题之二十三：从上到下打印二叉树
题目：从上到下打印二叉树的每个结点，同一层的结点按照从左到右的顺序打印

示例1：
输入
        3
       / \
     9   20
        /  \
       15   7

输出
    [3, 9, 20, 15, 7]

示例2:
输入
        1
       / \
      2   3
       \   \
        4   5

输出
    [1, 2, 3, 4, 5]

思路：使用队列
1) 初始化 res=[], queue=[root]
2) 队列不为空时，弹出结点，将结点的值添加到res中
3) 如果该结点的子结点存在，就把子结点加入队列
"""

from typing import List


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root: TreeNode) -> List:
    levels = []
    if root is None:
        return levels

    def helper(node: TreeNode, level: int) -> None:
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)

        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    res = []
    for level in levels:    # levels就是分层的结果，如果需要区分层树可以直接返回
        res += level

    return res


def level_order_v2(root: TreeNode) -> List:
    """使用队列"""
    if root is None:
        return []
    res, queue = [], [root]     # queue也可以使用queue模块里面的Queue
    while queue:
        node = queue.pop(0)
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    print(level_order_v2(node1))

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node6.left = node7
    node7.left = node8
    print(level_order_v2(node6))

    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node9.right = node10
    node10.right = node11
    print(level_order_v2(node9))

    node12 = TreeNode(12)
    print(level_order_v2(node12))

    print(level_order_v2(None))

    node13 = TreeNode(1)
    node14 = TreeNode(2)
    node15 = TreeNode(3)
    node16 = TreeNode(4)
    node17 = TreeNode(5)
    node13.left = node14
    node13.right = node15
    node14.right = node16
    node15.right = node17
    print(level_order_v2(node13))
