class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target >= nums[len(nums)//2]:
                for i, v in enumerate(nums[len(nums)//2:]):
                    if v > target:
                        return i+len(nums[:len(nums)//2])
                else:
                    return len(nums)
            else:
                for i, v in enumerate(nums[:len(nums)//2+1]):
                    if v > target:
                        return i                    