from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        common = Counter(nums).most_common(1)[0][0]
        nums_origin = [i for i in range(1, len(nums)+1)]
        answer = [common, list(set(nums_origin)-set(nums))[0]]
        
        return answer