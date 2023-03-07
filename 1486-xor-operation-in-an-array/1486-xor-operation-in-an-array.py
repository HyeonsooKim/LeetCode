class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*x for x in range(n)]
        ans = nums[0]
        for i in nums[1:]:
            ans ^= i
            
        return ans