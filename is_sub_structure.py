#!/usr/bin/env python3
# coding: utf-8

"""
面试题之十八：树的子结构
题目：输入两颗二叉树A和B，判断B是不是A的子结构

样例1：
树A:
        3
       / \
      4   5
     / \
    1   2

树B:
       4
      /
     1
注意：判定的是子结构而不是子树！此处B是A的子结构
"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_sub_structure(A: TreeNode, B: TreeNode) -> bool:
    res = False
    if A is not None and B is not None:
        # 如果根结点的值相同，就判断A的子树中是否有与B相同的结构
        # 有就直接返回True,没有就在A的左右子树中分别递归判断
        if A.val == B.val:
            res = treeA_have_treeB(A, B)
        if not res:
            res = is_sub_structure(A.left, B)
        if not res:
            res = is_sub_structure(A.right, B)

    return res


def treeA_have_treeB(A: TreeNode, B: TreeNode) -> bool:
    """
    判断A中是否有与B相同的结构
    有返回True，否则返回False
    """
    if B is None:
        return True
    if A is None:
        return False
    if A.val != B.val:
        return False

    return treeA_have_treeB(A.left, B.left) and treeA_have_treeB(A.right, B.right)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    node8 = TreeNode(2)
    node9 = TreeNode(4)
    node10 = TreeNode(5)
    node8.left = node9
    node8.right = node10
    print(is_sub_structure(node1, node8))
