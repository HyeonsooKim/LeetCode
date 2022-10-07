class Solution:
    def isValid(self, s: str) -> bool:
        
        s_list = list(s)
        stack = []
        result = True
 
        for s in s_list:
            if s == '(' or s =='{' or s == '[':
                stack.append(s)
            else:
                if len(stack) ==0:
                    result = False
                elif s ==')':
                    if stack.pop() != '(':
                        result = False
                elif s =='}':
                    if stack.pop() != '{':
                        result = False
                elif s ==']':
                    if stack.pop() != '[':
                        result = False
        
        if len(stack) !=0:
            result = False
 
        return result