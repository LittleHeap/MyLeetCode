"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None
        ol = []
        od = {}
        i = 0
        orign = node

        rl = []

        ocur = [node]
        while ocur:
            newocur = []
            while ocur:
                o = ocur.pop(0)
                if o not in od:
                    ol.append(o)
                    rl.append(Node(o.val, []))
                    od[o] = i
                    i += 1
                    for onei in o.neighbors:
                        newocur.append(onei)
            ocur = newocur

        for i in range(len(ol)):
            for nei in ol[i].neighbors:
                index = od.get(nei)
                rl[i].neighbors.append(rl[index])

        return rl[0]
