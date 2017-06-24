import re

class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.cur = 0
        self.strList = []
        p = re.compile(r'(\D\d+)')
        groups = p.findall(compressedString)

        for group in groups:
            num = int(group[1:])
            print 'num:'+str(num)
            for j in range(num):
                self.strList.append(group[0])


    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.cur += 1
            return self.strList[self.cur-1]
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur < len(self.strList):
            return True
        return False



        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()

if __name__ == '__main__':
    s = StringIterator('L1e2t1C1o1d1e11')
    while s.hasNext():
        print s.next()

    # p = re.compile(r'(\D\d)')
    # s = 'L1e2t1C1o1d1e1'
    # print p.findall(s)