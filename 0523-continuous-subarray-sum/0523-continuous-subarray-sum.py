class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_rem = dict({0:-1})
        prefix_sum = 0
        
        for i, v in enumerate(nums):
            prefix_sum = (prefix_sum+v) % k
            
            if prefix_sum in prefix_rem:
                if i - prefix_rem[prefix_sum] >= 2:
                    return True
            else:
                prefix_rem[prefix_sum] = i
        
        return False
        