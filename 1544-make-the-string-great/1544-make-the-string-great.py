class Solution:
    def makeGood(self, s: str) -> str:
        ls1 = [chr(i)+chr(i+32) for i in range(65,91)]
        ls2 = [chr(i+32)+chr(i) for i in range(65,91)]
        while True:
            ss = s
            for i in ls1: s = s.replace(i, '')
            for i in ls2: s = s.replace(i, '')
            if ss == s:
                break
        
        return s