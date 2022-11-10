class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if len(stk) > 0:
                if i != stk[-1]: stk.append(i)
                else: stk.pop()
            else:
                stk.append(i)
        
        return ''.join(stk)