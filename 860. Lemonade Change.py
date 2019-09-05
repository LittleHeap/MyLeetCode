bills = [5, 5, 5, 5, 20, 20, 5, 5, 5, 5]


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}

        for ele in bills:
            if d.get(5) < 0 or d.get(10) < 0:
                return False
            if ele == 5:
                d[ele] = d.get(ele) + 1
            elif ele == 10:
                d[ele] = d.get(ele) + 1
                d[5] = d.get(5) - 1
            else:
                d[ele] = d.get(ele) + 1
                if d.get(10) > 0:
                    d[10] = d.get(10) - 1
                    d[5] = d.get(5) - 1
                else:
                    d[5] = d.get(5) - 3

        if d.get(5) >= 0 and d.get(10) >= 0:
            return True
        else:
            return False
