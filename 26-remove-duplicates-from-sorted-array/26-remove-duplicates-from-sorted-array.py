class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rem_dup = list(set(nums))
        rem_dup.sort()
        for i in range(len(rem_dup)):
            nums[i] = rem_dup[i]
        return len(rem_dup)