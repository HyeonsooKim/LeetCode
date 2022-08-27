class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth = len(nums)
        for i in range(lenth-1):
            for j in range(i+1, lenth):
                if nums[i]+nums[j] == target:
                    return [i,j]
                else:
                    continue

# 다른 풀이 1
def twoSum(self, nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

# 다른 풀이 2
class Solution(object):
	def twoSum(self, nums, target):
		buffer_dictionary = {}
		for i in rangenums.__len()):
			if nums[i] in buffer_dictionary:
				return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the 
														#necesarry pair has been iterated on previously
			else: # else is entirely optional
				buffer_dictionary[target - nums[i]] = i 
				# we insert the required number to pair with should it exist later in the list of numbers