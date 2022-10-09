class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls = []
        for i in range(len(nums)):
            if nums[i] != val:
                ls.append(nums[i])
        
        for i in range(len(ls)):
            nums[i] = ls[i]
        
        return len(ls)