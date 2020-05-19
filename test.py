# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        from collections import defaultdict
        self.res = None
        self.dic, self.leaves = defaultdict(list), set()
        self.dfs(root)
        self.bfs(k)
        return self.res

    def dfs(self, root):
        '''Preorder through the Tree and construct graph'''
        if not root: return
        if not root.left and not root.right:
            self.leaves.add(root.val)
            return
        if root.left:
            self.dic[root.val].append(root.left.val)
            self.dic[root.left.val].append(root.val)
            self.dfs(root.left)
        if root.right:
            self.dic[root.val].append(root.right.val)
            self.dic[root.right.val].append(root.val)
            self.dfs(root.right)

    def bfs(self, k):
        '''Find the closest neighbor of k that is also a leaf'''
        q = [k]
        while q:
            new_q = []
            for node in q:
                if node in self.leaves:
                    self.res = node
                    return
                new_q += self.dic.pop(node, [])
            q = new_q