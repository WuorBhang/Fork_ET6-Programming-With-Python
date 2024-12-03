#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Swapping Values

Fill in the blanks to pass the assertions.

"""

a = 2
b = 1

assert a == 2, "a's initial value"
assert b == 1, "b's initial value"

temp = a
assert temp == a, "temp's final value"

a = 2
assert a == 2, "a's final value"

b = temp
assert b == temp, "b's final value"
