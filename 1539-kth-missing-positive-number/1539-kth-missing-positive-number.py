class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        while k:
            i += 1
            if i in arr:
                pass
            else:
                k -= 1
        
        return i