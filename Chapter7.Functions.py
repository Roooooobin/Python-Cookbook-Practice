"""
# -*- coding: utf-8 -*-
# @FileName: Chapter7.Functions.py
# @Author  : Robin
# @Time    : 2020/1/6 16:31
"""


def accept_any_number_of_arguments():
    def avg(first, *rest):
        return (first + sum(rest)) / (1 + len(rest))

    print(avg(1, 2, 3, 4))  # 2.5

    def foo(value, **attrs):
        return value, attrs

    print(foo(1, key1=2, key2=3))  # (1, {'key1': 2, 'key2': 3})
    """
    A * argument can only appear as the last positional argument
    A ** argument can only appear as the last argument
    """


# accept_any_number_of_arguments()


def only_keyword_arguments():
    """
    any arguments after a *-argument is considered as a keyword-only argument
    """

    def recv(maxsize, *, block):
        "Receives a message"
        pass

    # recv(1024, True)    # TypeError: recv() takes 1 positional argument but 2 were given
    recv(1024, block=True)
    """
    keyword-only arguments are often a good way to enforce greater code clarity
    when specifying optional function arguments
    """


# only_keyword_arguments()


def attaching_information_metadata():
    """
    annotations can be a useful way to give hints about how a function is supposed to use
    """
    def add(x: int, y: int) -> int:
        return x + y

    print(add(2, 3))
    print(add.__annotations__)  # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}


# attaching_information_metadata()


def anonymous_or_inline_functions():
    add = lambda x, y: x + y
    print(add(2, 3))
    """
    lambda is used in the context of some other operation, such as sorting or a data reduction
    """
    names = ["Robin Zhang", "Lebron James", "Anthony Davis"]
    print(sorted(names, key=lambda name: name.split()[-1].lower()))  # ['Anthony Davis', 'LeBron James', 'Robin Zhang']


# anonymous_or_inline_functions()


def anonymous_function_capture_value():
    x = 10
    a = lambda y: x + y
    print(a(10))    # 20
    x = 20
    print(a(10))    # 30
    """
    include the value as a default value to capture a value at the point of definition and keep it
    """
    b = lambda y, x=x: x + y
    print(b(10))    # 30
    x = 30
    print(b(10))    # 30

    funcs = [lambda x: x+n for n in range(3)]
    for f in funcs:
        print(f(0))
    """
    2
    2
    2
    """
    funcs2 = [lambda x, n=n: x+n for n in range(3)]
    for f in funcs2:
        print(f(0))
    """
    0
    1
    2
    """


# anonymous_function_capture_value()
