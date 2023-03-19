class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def dist(x1, y1, x2, y2):
            return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        
        ans = [0] * len(queries)
        for i in points:
            for idx, val in enumerate(queries):
                if dist(i[0], i[1], val[0], val[1]) <= val[2]:
                    ans[idx] += 1
                    
        return ans
                