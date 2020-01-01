"""
# -*- coding: utf-8 -*-
# @FileName: Chapter3.Numbers, Dates, and Times.py
# @Author  : Robin
# @Time    : 2020/1/1 20:15
"""


def binary_octal_hexadecimal():
    x = 1234
    print(bin(x))   # 0b10011010010
    print(oct(x))   # 0o2322
    print(hex(x))   # 0x4d2
    print(format(x, 'b'))   # 10011010010
    print(format(x, 'o'))   # 2322
    print(format(x, 'x'))   # 4d2


# binary_octal_hexadecimal()

def Working_with_Infinity_and_NaNs():
    """
    using float() to create inf and nan
    """
    a = float("inf")
    print(a)    # inf
    b = float("-inf")
    print(b)    # -inf
    c = float("nan")
    print(c)    # nan


# Working_with_Infinity_and_NaNs()

def fractions():
    from fractions import Fraction

    a = Fraction(3, 4)
    print(a)    # 3/4
    b = Fraction(5, 7)
    print(b)    # 5/7
    c = a * b
    print(c.numerator)  # 15
    print(c.denominator)    # 28


# fractions()
