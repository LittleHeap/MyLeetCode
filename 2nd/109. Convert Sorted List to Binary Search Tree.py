# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def func(l):
            if not l:
                return None
            index = len(l) // 2
            node = TreeNode(l[index])
            node.left = func(l[:index])
            node.right = func(l[index + 1:])
            return node

        return func(nums)