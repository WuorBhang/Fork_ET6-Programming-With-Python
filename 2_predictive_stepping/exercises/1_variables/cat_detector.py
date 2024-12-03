#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the user for the input "cat", throws an assertion error if the input is wrong
"""

maybe_cat = input('Enter "cat": ')

is_cat = maybe_cat == "cat"

# This assertion will bring an error if is_cat is False/not cat as input
assert is_cat, 'You should have entered "cat"'

# The results after writing the cat will be printed the thank you message.
print("Thank you for the cat!")