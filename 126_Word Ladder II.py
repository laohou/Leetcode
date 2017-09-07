# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given two words (beginWord and endWord), and a dictionary's word list,

find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list.
Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).

Please reload the code definition to get the latest changes.
"""

class LinkListNode:
    def __init__(self, val):
        self.val = val
        self.prev = []


from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        results = deque()
        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        cur_level = [LinkListNode(beginWord)]
        next_level = []
        depth = 1
        word_len = len(beginWord)
        word_list_dict = {}

        for word in wordList:
            word_list_dict[word] = 0

        while cur_level:
            for item in cur_level:
                if item.val == endWord:
                    self.add_path(results, item)
                useless_nodes = set()
                for i in xrange(word_len):
                    for char in all_chars:
                        new_word = item.val[:i] + char + item.val[i + 1:]
                        if new_word in word_list_dict:
                            new_node = LinkListNode(new_word)
                            new_node.prev.append(item)
                            #word_list_dict.pop(new_word)
                            useless_nodes.add(new_word)
                            next_level.append(new_node)

                for w in useless_nodes:
                    word_list_dict.pop(w)

            cur_level = next_level
            next_level = []
            depth += 1

        return results

    def add_path(self, results, item):
        if item:
            if len(results) == 0:
                results.appendleft(deque([item.val]))
            else:
                for result in results:
                    result.appendleft(item.val)
            if len(item.prev) > 0:
                for prev in item.prev:
                    self.add_path(results, prev)

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print Solution().findLadders(beginWord, endWord, wordList)