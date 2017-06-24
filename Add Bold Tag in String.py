class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        length = len(s)
        indexList = []
        for w in dict:
            wLen = len(w)
            for i in range(0, length-wLen+1):
                if s[i:i+wLen] == w:
                    indexList.append((i, i+wLen-1))

        print indexList
        indexList = sorted(indexList, key=lambda x:(x[0], x[1]))
        result = ''
        indexLen = len(indexList)
        i = 0
        prev = 0
        start, end = 0, 0
        if indexLen == 0:
            return s
        while i < indexLen:
            start, end = indexList[i]
            result += s[prev:start]

            while i<indexLen-1 and indexList[i+1][0]<=end+1:
                end = max(end, indexList[i+1][1])
                i += 1

            result = result +r'<b>'+s[start:end+1]+r'</b>'
            prev = end + 1
            i += 1
        result = result + s[end+1:length]
        return result



if __name__ == '__main__':
    solution = Solution()

    s = "abcxyz123"
    dict = ["abc", "123"]
    print solution.addBoldTag(s, dict)
    s = "aaabbcc"
    dict = ["aaa", "aab", "bc"]
    print solution.addBoldTag(s, dict)
    s = 'aabbcc'
    dict = []
    print solution.addBoldTag(s,dict)