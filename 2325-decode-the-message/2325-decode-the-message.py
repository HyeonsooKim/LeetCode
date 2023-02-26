class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        key = "".join(key.split())
        idx = 97
        for i in key:
            if i not in d.keys(): 
                d[i] = chr(idx)
                idx += 1
        
        ans = ""
        for i in message:
            if i == " ":
                ans += " "
            else:
                ans += d[i]
        
        return ans