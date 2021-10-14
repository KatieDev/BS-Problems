class Solution:
    def solve(self, nums):
        diff = 0
        nums.sort()
        for i in range(len(nums) - 1):
            diff = max(nums[i + 1] - nums[i], diff)
        return diff
            
#https://binarysearch.com/problems/Largest-Gap