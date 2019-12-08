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


def sort_dictionaries_by_common_key():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    """
    use itemgetter to sort
    """
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter("fname"))
    # rows_by_fname = sorted(rows, key=lambda x: x["fname"])
    rows_by_uid = sorted(rows, key=itemgetter("uid"))
    print(rows_by_fname)
    print(rows_by_uid)
    """
    itemgetter() can accept multiple keys
    can be replaced by lambda but itemgetter() is a bit faster
    """
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    # rows_by_lfname = sorted(rows, key=lambda x: (x["lname"], x["fname"]))
    print(rows_by_lfname)


# sort_dictionaries_by_common_key()


def attrgetter_():
    """
    use attrgetter to sort self-defined object
    """
    from operator import attrgetter
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

    users = [User(3), User(2), User(23)]
    sorted(users, key=attrgetter("user_id"))
    # sorted(users, key=lambda u: u.user_id)


def group_record_together_based_on_a_field():
    """
    itertools.groupby() to group data together(based on the key given)
    sort first
    """
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    from operator import itemgetter
    from itertools import groupby
    rows.sort(key=itemgetter("date"))
    for date, items in groupby(rows, key=itemgetter("date")):
        print(date)
        for i in items:
            print("   ", i)
    """
    07/01/2012
        {'address': '5412 N CLARK', 'date': '07/01/2012'}
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
    07/02/2012
        {'address': '5800 E 58TH', 'date': '07/02/2012'}
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
        {'address': '1060 W ADDISON', 'date': '07/02/2012'}
    07/03/2012
        {'address': '2122 N CLARK', 'date': '07/03/2012'}
    07/04/2012
        {'address': '5148 N CLARK', 'date': '07/04/2012'}
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
    """


# group_record_together_based_on_a_field()


def filter_compress():
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))
    print(ivals)
    # Outputs ['1', '2', '-3', '4', '5']

    """
    compress takes an iterable and an accompanying Boolean selector sequence as input. 
    As output, it gives you all of the items in the iterable where the corresponding element in the selector is True
    """
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    # use compress to make a list of items that count > 5
    from itertools import compress
    more5 = [n > 5 for n in counts]
    print(more5)
    # [False, False, True, False, False, True, True, False]
    print(list(compress(addresses, more5)))
    # ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']


# filter_compress()


def namedtuple_():
    """
    collections.namedtuple() is like struct in c
    """
    from collections import namedtuple
    User = namedtuple("User", ["name", "age"])
    user = User("robin", "21")
    print(user)
    print(user.name)
    print(user.age)
    """
    User(name='robin', age='21')
    robin
    21
    """
    """
    namedtuple is immutable, use _replace()
    """
    user._replace(age=22)
    print(user)


# namedtuple_()


def chainmap():
    from collections import ChainMap
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    print(c["z"])   # 3, duplicate keys, values from the first mapping


# chainmap()
