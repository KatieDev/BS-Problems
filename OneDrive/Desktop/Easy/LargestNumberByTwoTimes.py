class Solution:
    def solve(self, nums):
        largest = max(nums)
        nums.remove(largest)
        secLargest = max(nums)
        if largest > secLargest * 2:
            return True
        return False

#https://binarysearch.com/problems/Largest-Number-By-Two-Times