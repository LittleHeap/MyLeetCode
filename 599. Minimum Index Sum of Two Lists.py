class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d = defaultdict(list)

        for i, ele in enumerate(list1):
            d[ele].append(i)
        for i, ele in enumerate(list2):
            d[ele].append(i)

        cur = float('inf')
        res = []
        for name, l in d.items():
            if len(l) == 2 and sum(l) <= cur:
                cur = sum(l)
                res.append(name)

        return res