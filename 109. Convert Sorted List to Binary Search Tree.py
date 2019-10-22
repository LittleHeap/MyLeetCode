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

        res = []
        while head:
            res.append(head.val)
            head = head.next

        def deep(l):
            if not l:
                return None
            mid = len(l) // 2
            node = TreeNode(l[mid])
            node.left = deep(l[:mid])
            node.right = deep(l[mid + 1:])
            return node

        return deep(res)



