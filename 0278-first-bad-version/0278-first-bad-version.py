# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        result = 1
        while start <= end:
            mid = (start+end) // 2
            if isBadVersion(mid):
                end = mid - 1
                result = mid
            else:
                start = mid + 1
        
        return result
            
            