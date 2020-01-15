"""
# -*- coding: utf-8 -*-
# @FileName: Chapter6.Data Encoding and Processing.py
# @Author  : Robin
# @Time    : 2020/1/15 18:48
"""


def csv_data():
    import csv
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # process row
            pass
    # row will be a tuple, indexing might be confusing, so use namedtuple
    from collections import namedtuple
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple("Row", headings)
        for r in f_csv:
            row = Row(*r)
            print(row)
            # process row
    # read the data as a sequence of dicts
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row['Symbol'])
    """
    AA
    AIG
    AXP
    BA
    C
    CAT
    """
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]
    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


# csv_data()


def json_data():
    # 与pickle操作类似
    import json

    data = {
        'name': 'Robin',
        'age': 22,
        'gender': 'male',
    }
    json_str = json.dumps(data)
    data = json.loads(json_str)
