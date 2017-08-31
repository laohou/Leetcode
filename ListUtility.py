# -*- coding: utf-8 -*-
from __future__ import print_function
__author__ = 'yghou'


def print_list(node):
    tmp = node
    while tmp:
        if tmp.next:
            print('%d-->'%(tmp.val), end='')
        else:
            print('%d'%(tmp.val), end='')
        tmp = tmp.next