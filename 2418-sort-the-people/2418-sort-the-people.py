class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict()
        for i, j in zip(names, heights):
            d[j] = i
        
        sorted_dict = sorted(d.items(), key = lambda item:item[0], reverse=True)
        _names = []
        _heights = []
        for i in sorted_dict:
            _names.append(i[1])
            _heights.append(i[0])
        return _names