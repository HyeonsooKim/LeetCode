class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length1 = len(nums1)
        length2 = len(nums2)
        answer = []
        if length1 < length2:
            for i in nums1:
                if i in nums2:
                    answer.append(nums2.pop(nums2.index(i)))
        else:
            for i in nums2:
                if i in nums1:
                    answer.append(nums1.pop(nums1.index(i)))
        
        return answer