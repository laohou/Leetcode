import sys
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m < n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            return (nums1[m/2] + nums1[(m-1)/2])/2.0
        low = 0
        high = 2*n
        while low <= high:
            mid2 = (low + high) / 2
            mid1 = m + n - mid2
            L1,L2,R1,R2 = -sys.maxint-1, -sys.maxint-1, sys.maxint, sys.maxint
            if mid1 != 0:
                L1 = nums1[(mid1-1)/2]
            if mid2 != 0:
                L2 = nums2[(mid2-1)/2]
            if mid1 != 2*m:
                R1 = nums1[mid1/2]
            if mid2 != 2*n:
                R2 = nums2[mid2/2]

            if L1 > R2:
                low = mid2 + 1
            elif R1 < L2:
                high = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2.0
        return -1



if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2],[3,4])
    print s.findMedianSortedArrays([1, 2, 3], [3,3,4, 4])
    print s.findMedianSortedArrays([],[1])