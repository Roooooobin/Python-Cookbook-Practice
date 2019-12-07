# def f1(x, *args, y, z):
#     print(x, args, y, z)
#
#
# f1(1, 2, 3, 4, y=5, z=6)
#
#
# def f2(*x, **args):
#     print(x, args)
#
#
# f2(1, 2, 3, x=2, y=3, z=6)
# def add(x: int, y: int) -> int:
#     return x + y
#
#
# print(add(1, 3))
# print(add.__annotations__)


def f1(a, b=None):
    print(a, b)


f1(1, [1, 2])


print(chr(15+65))