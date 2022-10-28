class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth = len(nums)
        for i in range(lenth-1):
            for j in range(i+1, lenth):
                if nums[i]+nums[j] == target:
                    return [i,j]
                n = lenth-i-1
                m = lenth-j-1
                if nums[n]+nums[m] == target:
                    return [m, n]
                else:
                    continue