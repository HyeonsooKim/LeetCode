class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs = nums[:n]
        ys = nums[n:]
        ans = []
        for i,j in zip(xs, ys):
            ans.append(i)
            ans.append(j)
            
        return ans