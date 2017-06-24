class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]


        result = strs[0]
        i = 1
        prefixLen = len(strs[0])
        while i<length:
            wLen = len(strs[i])
            k = 0
            while k<wLen and k<prefixLen:
                if strs[i][k] == result[k]:
                    k += 1
                else:
                    break


            if prefixLen != k:
                prefixLen = k
                result = strs[i][:k]

            i += 1
        return result
if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(['1232222', '123abcdef1'])