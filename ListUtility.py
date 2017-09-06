# -*- coding: utf-8 -*-
from __future__ import print_function
__author__ = 'yghou'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(node):
    tmp = node
    while tmp:
        if tmp.next:
            print('%d-->'%(tmp.val), end='')
        else:
            print('%d'%(tmp.val), end='')
        tmp = tmp.next



def build_list(vals):
    head = ListNode(0)
    temp = head
    for val in vals:
        node = ListNode(val)
        temp.next = node
        temp = temp.next
    temp.next = None
    return head.next

test_list = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

test_list.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6