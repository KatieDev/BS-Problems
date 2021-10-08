# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        count = 1
        if node == None:
            return 0
        while node.next != None:
            count += 1
            node = node.next
        return count

#https://binarysearch.com/problems/Length-of-a-Linked-List