#!/usr/bin/env python3
# coding: utf-8

"""
用两个队列实现栈
题目：用两个队列实现栈，分别完成压入和弹出功能
"""

from queue import Queue


class Stack(object):

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        if self.queue1.empty():
            self.queue2.put(item)
        else:
            self.queue1.put(item)

    def pop(self):
        if self.queue1.empty() and self.queue2.empty():
            return "empty stack!"
        if self.queue1.empty():
            while not self.queue2.empty():
                item = self.queue2.get()
                if self.queue2.empty():
                    return item
                self.queue1.put(item)
        else:
            while not self.queue1.empty():
                item = self.queue1.get()
                if self.queue1.empty():
                    return item
                self.queue2.put(item)


if __name__ == "__main__":
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())

    print("--------------")

    s2 = Stack()
    print(s2.pop())
    s2.push(1)
    s2.push(2)
    print(s2.pop())
    s2.push(3)
    print(s2.pop())
    print(s2.pop())
    print(s2.pop())
