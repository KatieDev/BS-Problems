class Solution:
    def solve(self, nums, k):
        m = {}
        for i in range(len(nums)):
            if k - nums[i] in m.values():
                return True
            else:
                m[nums[i]] = nums[i]
        return False

#https://binarysearch.com/problems/Sum-of-Two-Numbers