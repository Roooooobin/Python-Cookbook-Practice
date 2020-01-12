"""
# -*- coding: utf-8 -*-
# @FileName: Chapter5.Files and I.py
# @Author  : Robin
# @Time    : 2020/1/12 20:10
"""


def open_files():
    # with : file will be closed automatically
    with open("somefile.txt", "rt") as f:
        data = f.read()
        data_lines = f.readlines()

    with open("somefile.txt", "wt") as f:
        pass
    """
    wt clear and overwrite
    at append to the end
    rb
    wb
    """
    with open('somefile.txt', 'rt', encoding='latin-1') as f:
        pass
    """
    by default, files are read/written using the system default text encoding, 
    as can be found in sys.getdefaultencoding(), utf-8 on most machines
    common encodings are ascii, latin-1, utf-8, and utf-16.
    """


def errors_when_open_files():
    # Replace bad chars with Unicode U+fffd replacement char
    f1 = open("somefile.txt", "rt", encoding="ascii", errors="replace")
    # Ignore bad chars entirely
    f2 = open("somefile.txt", "rt", encoding="ascii", errors="ignore")


def print_to_file():
    with open("somefile.txt", "rt") as f:
        print("Hello World!", file=f)


def print_with_different_seq_end():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=",")
    print('ACME', 50, 91.5, sep=",", end="!!\n")

