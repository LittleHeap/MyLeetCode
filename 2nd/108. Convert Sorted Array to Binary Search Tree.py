# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None

        index = len(nums) // 2
        root = TreeNode(nums[index])

        def deep(fa, l, left):
            if not l:
                return
            index = len(l) // 2
            ll = l[:index]
            rl = l[index + 1:]
            if fa is None:
                deep(root, ll, 1)
                deep(root, rl, 0)
            else:
                node = TreeNode(l[index])
                if left:
                    fa.left = node
                else:
                    fa.right = node
                deep(node, ll, 1)
                deep(node, rl, 0)

        deep(None, nums, None)
        return root