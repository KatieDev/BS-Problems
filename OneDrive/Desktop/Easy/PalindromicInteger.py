class Solution:
    def solve(self, num):
        strNum = str(num)
        s = []
        last = -1
        for i in strNum:
            s.append(i)
        for i in range(len(s)):
            first = i
            if s[first] != s[last]:
                return False
            else: 
                last -= 1
        return True

#https://binarysearch.com/problems/Palindromic-Integer/solutions