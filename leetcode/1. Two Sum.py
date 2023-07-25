# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for index, j in enumerate(nums[i+1:]):
                res = nums[i]+j
                if res == target:
                    output = [i, index+1+i]
        return output