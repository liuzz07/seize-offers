#!/usr/bin/env python3
# coding: utf-8

"""
面试题之七：用两个栈实现队列
题目：用两个栈实现队列，分别完成在尾部插入结点和在队列头部删除结点的功能
"""


class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "empty stack!"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class MyQueue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def append_tail(self, item):
        self.stack1.push(item)

    def delete_head(self):
        if not self.stack2.is_empty():
            return self.stack2.pop()
        if self.stack1.is_empty():
            return "empty queue!"
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


if __name__ == "__main__":
    q1 = MyQueue()
    q1.append_tail(1)
    q1.append_tail(2)
    q1.append_tail(3)
    print(q1.delete_head())
    print(q1.delete_head())
    print(q1.delete_head())
    print(q1.delete_head())

    print("-------------------")

    q2 = MyQueue()
    q2.append_tail(1)
    print(q2.delete_head())
    print(q2.delete_head())
    q2.append_tail(2)
    q2.append_tail(3)
    print(q2.delete_head())
