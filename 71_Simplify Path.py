# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""

class Solution(object):
    def simplifyPathOld(self, path):
        """
        :type path: str
        :rtype: str
        """

        length = len(path)
        path_stack = []
        i = 0
        while i < length-1:
            if path[i] == '.':
                if path[i+1] == '.':
                    i += 1
                    while len(path_stack) > 0:
                        if path_stack[-1] == '/':
                            path_stack.pop()
                            break
                        path_stack.pop()

                #如果path[i]就是一个"."，就是值当前目录，啥都不会改变
            elif path[i] == '/':
                #如果path[i]就是一个"/"，后面如果是字母就入栈，否则就不入栈
                if path[i+1].isalpha():
                    path_stack.append(path[i])
            elif path[i].isalpha():
                path_stack.append(path[i])
            i += 1

        if path == length-1:
            if path[i].isalpha():
                path_stack.append(path[i])
        if len(path_stack) == 0:
            return '/'

        return ''.join(path_stack)



    def simplifyPath(self, path):
        """
        需要考虑到path 可能存在 ...的情况
        :type path: str
        :rtype: str
        """

        paths = path.split('/')
        path_stack = []

        for part in paths:
            if part:
                if part not in ('.', '..'):
                    if len(path_stack) == 0:
                        path_stack.append('')
                    path_stack.append(part)
                elif part == '..' and len(path_stack) > 0:
                    path_stack.pop()

        if len(path_stack) < 2:
            return '/'

        return '/'.join(path_stack)

if __name__ == '__main__':
    print Solution().simplifyPath('/home/')
    print Solution().simplifyPath('/a/./ssb/../../c/')
    print Solution().simplifyPath('/home//foo/')
    print Solution().simplifyPath('/')
    assert Solution().simplifyPath("/../../") == "/"
    assert Solution().simplifyPath("/...") == "/..."
    assert Solution().simplifyPath("///eHx/..") == "/"