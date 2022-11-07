class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = [num]
        ls = list(str(num))
        for i in range(len(ls)):
            if ls[i] == '6':
                temp = ls[:i]+['9']+ls[i+1:]
            else:
                temp = ls[:i]+['6']+ls[i+1:]
            ans.append(int(''.join(temp)))
        return max(ans)
            