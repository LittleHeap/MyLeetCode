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

        if not head:
            return None

        res = []
        while head:
            res.append(head.val)
            head = head.next
        hold = set()

        def deep(l, r):
            if r - l <= 1:
                if l >= len(res):
                    return None
                if res[l] not in hold:
                    hold.add(res[l])
                    return TreeNode(res[l])
                else:
                    return None
            mid = (l + r) // 2
            node = TreeNode(res[mid])
            hold.add(res[mid])
            node.left = deep(l, mid)
            node.right = deep(mid + 1, r)
            return node

        return deep(0, len(res))
