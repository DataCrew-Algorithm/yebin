#1. Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]'''

#v1
class Solution:
    def twoSum(self, nums):
        for i in nums:
            for j in nums:
                if i + j == target:
                        return nums.index(i), nums.index(j)


nums = [3,3]
target = 6
#Output: [0,1]
sol = Solution()
print(sol.twoSum(nums))

#v2 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                        return i,j