class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return 0
        if z == 0:
            return 1
        if x == 0 and y == 0:
            return 0
        if x == 0:
            if z % y == 0:
                return 1
            else:
                return 0
        if y == 0:
            if z % x == 0:
                return 1
            else:
                return 0
        if z % math.gcd(x, y) == 0:
            return 1
        else:
            return 0