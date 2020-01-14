"""
# -*- coding: utf-8 -*-
# @FileName: Chapter5.Files and IO.py
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


def write_to_file_doesnot_already_exist():
    with open("somefile", "xt") as f:
        pass
    """
    xt xb
    """


def read_write_compressed_files():
    import gzip, bz2
    with gzip.open("somefile.gz", "rt") as f:  # wt, rb, wb
        text = f.read()

    with bz2.open("somefile.bz2", "rt") as f:
        text = f.read()

    with gzip.open("somefile.gz", "wt", compresslevel=5) as f:
        pass
    """
    set compresslevel default: 9 which provides the highest level
    """


def readinto_buffer():
    import os.path

    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf

    record_size = 32
    buf = bytearray(record_size)
    with open("somefile", "rb") as f:
        while True:
            n = f.readinto(buf)     # return the number of bytes actually read
            if n < record_size:
                break
            # use the content of buf


def manipulate_pathnames():
    import os

    path = "/Users/robin/Data/data.csv"
    print(os.path.basename(path))
    print(os.path.dirname(path))
    """
    data.csv
    /Users/robin/Data
    """
    # split the file extension
    print(os.path.split(path))  # ('/Users/robin/Data', 'data.csv')
    # expand the user's home directory
    path = "~/Data/data.csv"
    print(os.path.expanduser(path))  # C:/Users/robin/Data/data.csv


# manipulate_pathnames()


def test_for_the_existence_of_a_file():
    import os
    path = os.path.join(os.getcwd(), "Chapter5.Files and IO.py")
    print(os.path.exists(path))
    print(os.path.isfile(path))
    print(os.path.isdir(path))
    print(os.path.getsize(path))
    print(os.path.getmtime(path))
    import time
    print(time.ctime(os.path.getmtime(path)))


# test_for_the_existence_of_a_file()


def directory_listing():
    import os
    print(os.getcwd())
    file_names = os.listdir(os.getcwd())
    print(file_names)
    # filename matching: glob or fnmatch
    import glob
    pyfiles = glob.glob("*5*.py")
    print(pyfiles)  # ['Chapter5.Strings and Text.py']
    from fnmatch import fnmatch
    pyfiles = [name for name in os.listdir(os.getcwd()) if fnmatch(name, "*5*.py")]
    print(pyfiles)  # ['Chapter5.Strings and Text.py']
    # meta data of a file
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)


# directory_listing()


def wrapping_existing_file_descriptor_as_file_object():
    """
    a file descriptor is different than a normal open file in that it is simply an integer handle assigned by the os
    """
    import os

    fd = os.open("somefile.txt", os.O_WRONLY | os.O_CREAT)

    f = open(fd, "wt")
    f.write("hello world\n")
    f.close()


def temporary_file():
    from tempfile import TemporaryFile, NamedTemporaryFile

    with TemporaryFile("w+t") as f:
        f.write()
        f.write()
        f.seek(0)
        data = f.read()

    # name of the temporary file
    with NamedTemporaryFile("w+t") as f:
        print(f.name)

    # auto delete closed
    with NamedTemporaryFile("w+t", delete=False) as f:
        pass

    # temporary directory
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as dirname:
        print(dirname)


def serialize_python_object():
    import pickle

    data = {"a": 1, "b": 2}     # any python object
    f = open("somefile", "wb")
    pickle.dump(data, f)
    f = open("somefile", "rb")
    data = pickle.load(f)
    # dump an object to string
    s = pickle.dumps(data)
    print(s)
    data = pickle.loads(s)
    print(data)
    # also able to work with restoring multiple objects
    # pickle functions, classes and instances but the resulting data only encodes name references to the code objects
    import math
    s = pickle.dumps(math.cos)
    cos_ = pickle.loads(s)
    print(cos_(2))


# serialize_python_object()
