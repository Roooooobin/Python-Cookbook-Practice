"""
# -*- coding: utf-8 -*-
# @FileName: Chapter2.Strings and Text.py
# @Author  : Robin
# @Time    : 2019/12/13 19:27
"""

import re


def split_strings():
    """
    re.split(pat, string)
    r'[\s,;]\s*'
    """
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    words = re.split(r'[\s,;]\s*', line)
    print(words)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    """
    capture group enclosed in parentheses
    gather delimiters as well
    """
    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    """
    ?:... to exclude separators in the result
    """
    fields = re.split(r'(?:,|;|\s)\s*', line)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    print(fields)


# split_strings()


def startswith_endswith():
    """
    use tuple to check against multiple choices
    """
    choices = ["http", "https"]
    url = "https:rooobin.top"
    print(url.startswith(tuple(choices)))  # True


# startswith_endswith()


def match_search_for_text_pattern():
    """
    startswith/endswith
    re.match(match() always tries to find the match at the start of a string)
    """
    text1 = "12/13/2019"
    if re.match(r'\d+/\d+/\d+', text1):  # True
        print(True)
    else:
        print(False)
    date_pattern = re.compile(r'\d+/\d+/\d+')  # True
    if date_pattern.match(text1):
        print(True)
    else:
        print(False)
    """
    re.findall(pat, text) / pat.findall(text) to return all matches
    re.findall(pat, text, flags=re.IGNORECASE)
    () to capture groups
    """
    text = "Today is 12/13/2019. Yesterday is 12/12/2019"
    ret = date_pattern.findall(text)
    print(ret)  # ['12/13/2019', '12/12/2019']
    date_pattern_capture = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = date_pattern_capture.match("12/13/2019")
    print(m.group(0))   # remember 0 is all, 1 is the first capture part of the group
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    """
    12/13/2019
    12
    13
    2019
    """
    # If you want to find matches iteratively, use the finditer() method instead
    for m in date_pattern_capture.finditer(text):
        print(m.groups())
    """
    ('12', '13', '2019')
    ('12', '12', '2019')
    """


# match_search_for_text_pattern()


def search_replace():
    """
    str.replace(str_before, str_after)
    re.sub(pat_before, pat_after, text)     \2, \1 to capture part of the group
    pat_before.sub(pat_after, text)
    subn to get the number of substitutions
    """
    text = "yeah, but no, but yeah, but no, but yeah"
    text.replace("yeah", "yep")

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))  # Today is 2012-11-27. PyCon starts 2013-3-13.


# search_replace()


def greedy_nongreedy_match():
    """
    greedy match by default, ? modifier after the * operator in the pattern
    """
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))
    """
    ['no.']
    ['no." Phone says "yes.']   # wrong results(.* tends to get the longest possible match)
    """
    str_pat_nongreedy = re.compile(r'\"(.*?)\"')
    print(str_pat_nongreedy.findall(text2))  # ['no.', 'yes.']


# greedy_nongreedy_match()
