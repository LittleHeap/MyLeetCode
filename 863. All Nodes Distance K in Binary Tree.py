# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        res = []

        def deep(node, level, res):
            if not node:
                return (defaultdict(list), None)
            else:
                ld, lt = deep(node.left, level + 1, res)
                rd, rt = deep(node.right, level + 1, res)
                cur = defaultdict(list)
                for ele in rd:
                    cur[ele] += rd[ele]
                for ele in ld:
                    cur[ele] += ld[ele]
                cur[level] += [node.val]
                if node == target:
                    res += cur[level + K]
                    return (cur, level)
                elif lt is not None:
                    res += ([node.val] if level + K == lt else [])
                    res += rd[level + K - lt + level]
                    return (cur, lt)
                elif rt is not None:
                    res += ([node.val] if level + K == rt else [])
                    res += ld[level + K - rt + level]
                    return (cur, rt)
                return (cur, None)

        deep(root, 1, res)
        return list(set(res))