class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(i):
                if j == 0 or j == (i-1):
                    temp.append(1)
                else:
                    temp.append(answer[-1][j-1] + answer[-1][j])
            answer.append(temp)
        return answer