#!/usr/bin/env python3
# coding: utf-8

"""
面试题之六：重建二叉树
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树，输出二叉树的头结点
"""

from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_binary_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """重建二叉树"""
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        root = TreeNode(preorder[0])
        return root
    index = inorder.index(preorder[0])
    left_child_preorder = preorder[1:index + 1]
    right_child_preorder = preorder[index + 1:]
    left_child_inorder = inorder[:index]
    right_child_inorder = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_binary_tree(left_child_preorder, left_child_inorder)
    root.right = construct_binary_tree(right_child_preorder, right_child_inorder)

    return root


def level_order_travel(root: TreeNode) -> List:
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


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = [1, 2, 4, 8, 9, 14, 5, 10, 11, 3, 6, 12, 13, 7]
    inorder = [8, 4, 14, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 7]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = [1, 2, 3]
    inorder = [1, 3, 2]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = [2]
    inorder = [2]
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))

    preorder = []
    inorder = []
    root = construct_binary_tree(preorder, inorder)
    print(level_order_travel(root))
