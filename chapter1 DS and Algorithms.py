# 巧妙实现递归
# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head
# print(sum([1, 2, 3]))

# from collections import deque
# q = deque(maxlen=2)
# q.append(1)
# q.append(2)
# q.append(23)
# q = list(q)
# print(q)
# import heapq
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1
#     def pop(self):
#          return heapq.heappop(self._queue)[-1]
#
# q = PriorityQueue()
# q.push('r', 2)
# q.push('y', 23)
# q.push('x', 22)
# q.push('s', 2)
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())

# values = ['1', '2', '-3', 'N/A', '...']
# def isInt(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
# ivals = list(filter(isInt, values))
# print(ivals)
# from collections import namedtuple
#
# _STU = namedtuple("_STU", ['number', 'grade'])
# stus = []
# stus.append(_STU('101', '100'))
# stus.append(_STU('1051', '80'))
# stus.append(_STU('1015', '70'))
# stus[0] = stus[0]._replace(number='1016')
# print(stus)
# from collections import ChainMap
# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# c = ChainMap(a, b)
# print(c)

