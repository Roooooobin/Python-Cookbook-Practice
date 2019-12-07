"""
# -*- coding: utf-8 -*-
# @FileName: Chapter1.Data Structures and Algorithms.py
# @Author  : Robin
# @Time    : 2019/12/7 19:05
"""


def sum_iter(items):
    """
    use unpacking to carry out clever recursive algorithm
    """
    head, *tail = items
    return head + sum(tail) if tail else head


# print(sum_iter([1, 2, 3]))    # output: 6


def keep_last_n_items():
    """
    use deque in collections to create a fixed-sized queue(set maxlen)
    when the queue is full, the oldest item is automatically removed
    """
    from collections import deque
    q = deque(maxlen=2)
    q.append(1)
    q.append(2)
    q.append(23)
    q = list(q)
    print(q)


# keep_last_n_items()   # output: [2, 23]


def find_largestorsmallest_n_items():
    """
    use functions(nlargest(), nsmallest()) to make a list of largest or smallest N items in a collection
    use sorting if N is close the size of the input
    """
    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
    """
    also key parameter that allows them to be used with more complicated DS
    """
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    # [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09},
    # {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
    print(expensive)
    # [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65},
    # {'name': 'IBM', 'shares': 100, 'price': 91.1}]


# find_largestorsmallest_n_items()


def heap():
    """
    detailed heapq utils in collections
    heap[0] is always the smallest item
    heappop() pops off the smallest and replace it with the next smallest item
    """
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    import heapq
    heap = list(nums)
    heapq.heapify(heap)  # turn heap into a list where items are ordered as a heap

    print(heapq.heappop(heap))  # -4
    print(heapq.heappop(heap))  # 1
    heapq.heappush(heap, -5)
    print(heapq.heappop(heap))  # -5


# heap()

import heapq


class PriorityQueue:
    """
    same priority return in the same order in which they were inserted into the queue
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def priority_queue():
    q = PriorityQueue()
    q.push('r', 2)
    q.push('y', 23)
    q.push('x', 22)
    q.push('s', 2)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


# priority_queue()


def defaultdict():
    """
    A feature of defaultdict is that it automatically initializes the first value so you can simply focus on adding items
    """
    from collections import defaultdict
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(d)


# defaultdict()


def determine_the_most_frequent():
    """
    use Counter in collections
    most_common(num=n) to determine the most frequent n items (item, number of occurrence)
    a Counter is a dictionary that maps the items to the number of occurrences
    """
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs: [('eyes', 8), ('the', 5), ('look', 4)]
    top_ten = word_counts.most_common(10)
    print(top_ten)
    # Outputs: [('eyes', 8), ('the', 5), ('look', 4), ('into', 3), ('my', 3), ('around', 2), ('not', 1), ("don't", 1), ("you're", 1), ('under', 1)]
    word_counts.update(["into", "look"])    # increment
    """
    combine or subtract counts
    """


# determine_the_most_frequent()
