# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if points == None:
            return 0
        return 0

if __name__ == "__main__":
    a = Point(1,1)
    b = Point(2,2)
    c = Point(1,1)
    print a==b
    print a.x==c.x and a.y==c.y
            
    
