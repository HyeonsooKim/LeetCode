class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        cnt = 0
        for i,v in enumerate(nums):
            if v == 0:
               cnt += 1
            else:
                ans.append(v)
        
        nums[:] = ans + [0] * cnt