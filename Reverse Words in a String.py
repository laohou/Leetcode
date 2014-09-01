class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split(None,-1)
        print len(words)
        print words
        result=""
        wordsLen = len(words)
        if wordsLen < 2:
            return ""
        for i in range(wordsLen-1,-1,-1):
            result +=words[i]
            result +=" "
        return result   

if __name__ == "__main__":
    solution = Solution()
    print solution.reverseWords("")
    print solution.reverseWords("  ")
    print solution.reverseWords("hello world adsd")
