class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i, c in enumerate(command):
            if c == '(':
               pass
            elif c == ')':
                if command[i-1] == '(':
                    ans += 'o'
            else:
                ans += c
                
        
        return ans