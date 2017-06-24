import re

class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.cur = 0
        self.groupList = []
        self.strLen = 0
        self.groupIndex = 0
        self.prevGroupSizes = 0
        p = re.compile(r'(\D\d+)')
        groups = p.findall(compressedString)

        for group in groups:
            num = int(group[1:])
            self.strLen += num
            self.groupList.append((group[0], num))

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            groupSize = self.groupList[self.groupIndex][1]
            self.cur += 1
            if self.cur > self.prevGroupSizes+groupSize:
                self.prevGroupSizes += groupSize
                self.groupIndex += 1

            return self.groupList[self.groupIndex][0]

        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur < self.strLen:
            return True
        return False



        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()

if __name__ == '__main__':
    s = StringIterator('L1e2t1C11o1d1e1')
    #s = StringIterator('a123')
    i = 1
    while s.hasNext():
        print 'line:', str(i)
        print s.next()
        i += 1

    # p = re.compile(r'(\D\d)')
    # s = 'L1e2t1C1o1d1e1'
    # print p.findall(s)