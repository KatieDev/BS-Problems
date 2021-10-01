class Solution:
    def solve(self, s):
        m = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) + 1
            if m[s[i]] > 1:
                return False
        return True
        
#https://binarysearch.com/problems/A-Unique-String