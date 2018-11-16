# coding=utf-8
# Given an array of strings, return all groups of strings that are anagrams.

# Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].
# Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
import numpy as np

def groups(alist):
    res = {}

    for i in alist:
        item = ''.join(sorted(i))   # sorted出来是'l', 's'的字符
        res[item] = res[item]+[i] if item in res.keys() else [i]
    print res


groups(["lint", "intl", "inlt", "code"])