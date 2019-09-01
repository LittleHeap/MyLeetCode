# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        a = l.copy()
        a.reverse()
        if a == l:
            return True
        else:
            return False
