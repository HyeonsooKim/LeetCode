class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:  # binary search: O(log n)
        left, right = 0, len(nums)  # no len(nums) - 1, as we might need to insert at the end of the array
        while left < right:
            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left