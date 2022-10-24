class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = []
        for i in arr:
            u = set(i)
            if len(u) == len(i):
                unique.append(u)
        
        concat = [set()]
        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append(c | u)
        
        return max([len(a) for a in concat])
                    
        
                
        