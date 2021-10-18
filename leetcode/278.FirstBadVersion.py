# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start,end = 1,n
        
        while start<=end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid - 1 
            else:
                start = mid + 1
                
        return start
        