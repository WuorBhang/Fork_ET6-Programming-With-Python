#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Fix the bug(s)! """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from trace_recursion import trace_recursion
except ImportError:
    import functools
    def trace_recursion(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


@trace_recursion
def fibonacci_memo(n: int, memo: dict = {}) -> int:
    """
    
    """
    if n == 0:
        return 0

    if n == 1:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)    
    return memo[0]


# --- call the traced function ---

print(fibonacci_memo(0), 'should be', 0)
print(fibonacci_memo(1), 'should be', 1)
print(fibonacci_memo(2), 'should be', 1)
print(fibonacci_memo(3), 'should be', 2)
print(fibonacci_memo(4), 'should be', 3)
print(fibonacci_memo(6), 'should be', 8)
print(fibonacci_memo(8), 'should be', 21)
