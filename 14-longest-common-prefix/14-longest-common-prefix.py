class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        answer = ''
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for j in strs:
                if shortest[i] != j[i]:
                    return answer
            else:
                answer += shortest[i]
        else:
            return answer