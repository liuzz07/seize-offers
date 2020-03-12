#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十九：二叉树的镜像
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像

示例
输入：
        4
       / \
      2   7
     / \ / \
    1  3 6  9

输出：
        4
       / \
      7   2
     / \ / \
    9  6 3  1

"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mirror_of_binarytree(root: TreeNode) -> TreeNode:
    """递归"""
    if root is None:
        return
    if root.left is None and root.right is None:
        return root

    root.left, root.right = mirror_of_binarytree(root.right), mirror_of_binarytree(root.left)

    return root


def mirror_of_binarytree_v2(root: TreeNode) -> TreeNode:
    """循环, 前序遍历"""
    if root is None:
        return
    if root.left is None and root.right is None:
        return root

    stack = []
    node = root
    while node is not None or stack:
        if node is not None:
            node.left, node.right = node.right, node.left
            stack.append(node)  # 注意是把node加入而不是node.right
            node = node.left
        else:
            node = stack.pop()
            node = node.right  # 处理右子树

    return root


def level_order_travel(root: TreeNode):
    """输出宽度优先遍历的结果，用于验证"""
    levels = []
    if not root:
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
    return levels


if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node = mirror_of_binarytree_v2(node1)
    print(level_order_travel(node))

    node8 = TreeNode(5)
    node = mirror_of_binarytree_v2(node8)
    print(level_order_travel(node))

    node = mirror_of_binarytree_v2(None)
    print(level_order_travel(node))

    node9 = TreeNode(2)
    node10 = TreeNode(7)
    node11 = TreeNode(8)
    node9.left = node10
    node10.right = node11
    node = mirror_of_binarytree_v2(node9)
    print(level_order_travel(node))
