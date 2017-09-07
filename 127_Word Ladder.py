# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).

Please reload the code definition to get the latest changes.
"""


from collections import defaultdict

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        cur_level = [beginWord]
        next_level =[]
        depth = 1
        word_len = len(beginWord)
        word_list_dict = {}
        for word in wordList:
            word_list_dict[word] = 0

        while cur_level:
            for item in cur_level:
                if item == endWord:
                    return depth
                for i in xrange(word_len):
                    for char in all_chars:
                        new_word = item[:i] + char + item[i + 1:]
                        if new_word in word_list_dict:
                            word_list_dict.pop(new_word)
                            next_level.append(new_word)

            cur_level = next_level
            next_level = []
            depth += 1

        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print Solution().ladderLength(beginWord, endWord, wordList)