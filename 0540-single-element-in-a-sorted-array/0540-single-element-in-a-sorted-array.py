from collections import Counter, OrderedDict
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return list(OrderedDict(Counter(nums).most_common()))[-1]

        