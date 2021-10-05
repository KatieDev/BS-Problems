class Solution:
    def solve(self, nums):
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 != 0:
                count += 1
        return count

#https://binarysearch.com/problems/Odd-Number-of-Digits