class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        for i, v in enumerate(nums):
            if v not in dup:
                dup.append(v)
        
        for i in range(len(dup)):
            nums[i] = dup[i]
            
        return len(dup)