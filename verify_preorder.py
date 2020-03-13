#!/usr/bin/env python3
# coding: utf-8

"""
补充：二叉搜索树的前序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果
如果是返回True，否则返回False。假设输入的数组任意两个数字都不相同
"""


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def verify_preorder(preorder: TreeNode) -> bool:
    if not preorder or len(preorder) == 1:
        return True

    left = []
    i = 1
    while i < len(preorder) and preorder[i] < preorder[0]:
        left.append(preorder[i])
        i += 1
    right = preorder[i:]
    for item in right:
        if item <= preorder[0]:
            return False

    return verify_preorder(left) and verify_preorder(right)


if __name__ == "__main__":
    preorder = [7, 2, 4, 9, 8]
    print(verify_preorder(preorder))

    preorder = [5, 7, 3, 2, 9]
    print(verify_preorder(preorder))

    preorder = [2, 5, 9, 1, 0]
    print(verify_preorder(preorder))

    preorder = [6, 8]
    print(verify_preorder(preorder))

    preorder = [6]
    print(verify_preorder(preorder))

    preorder = []
    print(verify_preorder(preorder))
