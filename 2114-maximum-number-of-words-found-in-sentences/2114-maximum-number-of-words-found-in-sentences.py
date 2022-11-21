class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ls = [len(i.split()) for i in sentences]
        return max(ls)