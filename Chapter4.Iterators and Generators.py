"""
# -*- coding: utf-8 -*-
# @FileName: Chapter4.Iterators and Generators.py
# @Author  : Robin
# @Time    : 2020/1/2 21:32
"""


def generate_permutations():
    from itertools import permutations
    from itertools import combinations
    from itertools import combinations_with_replacement

    for p in permutations([1, 2, 3]):
        print(p)
    """
    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)
    """
    for p in permutations([1, 2, 3], 2):
        print(p)
    """
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
    """
    for c in combinations([1, 2, 3], 3):
        print(c)
    """
    (1, 2, 3)
    """
    for c in combinations_with_replacement([1, 2, 3], 3):
        print(c)
    """
    (1, 1, 1)
    (1, 1, 2)
    (1, 1, 3)
    (1, 2, 2)
    (1, 2, 3)
    (1, 3, 3)
    (2, 2, 2)
    (2, 2, 3)
    (2, 3, 3)
    (3, 3, 3)
    """


# generate_permutations()

def chain_iteration():
    """
    use chain() to iterate on items in separate containers, chain(a, b) more elegant and efficient than a+b
    """
    from itertools import chain

    a = [1, 2, 3, 4]
    b = ['a', 'b', 'c']
    for x in chain(a, b):
        print(x)


# chain_iteration()
