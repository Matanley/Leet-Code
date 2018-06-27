"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def two_sum(self, nums, target):
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
solution = []
base = 0
while base < len(nums):
	for index in range(base + 1, len(nums)):
	    if nums[base] + nums[index] == target:
	        solution.append(base)
	        solution.append(index)
	base += 1
return solution