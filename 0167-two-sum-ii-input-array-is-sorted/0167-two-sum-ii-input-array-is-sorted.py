class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        start = 0
        end = len(numbers) - 1
        while start<end:
            if numbers[start]+numbers[end] == target:
                answer.append(start+1)
                answer.append(end+1)
                break
            if numbers[start]+numbers[end] < target:
                start += 1
            else:
                end -= 1
        
        return answer