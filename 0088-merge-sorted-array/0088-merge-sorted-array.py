class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        if m == 0:
            nums1[:] = nums2
        else:
            nums1[:] = sorted(nums1[:m]+nums2[:n])