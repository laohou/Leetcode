# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""


class Solution(object):

    def restoreIpAddressRecur(self, length, ips, s, result):
        if not s:
            if length == 4:
                result.append(".".join(ips))
            return
        elif length == 4:
            return

        self.restoreIpAddressRecur(length+1, ips+[s[:1]], s[1:], result)

        if s[0] != '0':
            if len(s) >= 2:
                self.restoreIpAddressRecur(length+1, ips+[s[:2]], s[2:], result)
            if len(s) >= 3 and int(s[:3]) < 256:
                self.restoreIpAddressRecur(length+1, ips+[s[:3]], s[3:], result)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length > 12 or length < 4:
            return []
        result = []
        self.restoreIpAddressRecur(0, [], s, result)
        return result




if __name__ == '__main__':
    print Solution().restoreIpAddresses('25525511135')
    print Solution().restoreIpAddresses('1111')