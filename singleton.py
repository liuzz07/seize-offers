#!/usr/bin/env python3
# coding: utf-8

'''
面试题之二：实现Singleton模式
'''

import threading


class Singleton(object):
    _instance = None
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with cls._instance_lock:
            cls._instance = object.__new__(cls)
        return cls._instance
