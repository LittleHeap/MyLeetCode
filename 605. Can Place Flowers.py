class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        m = len(flowerbed)

        for i in range(m):
            if n == 0:
                return True
            if i == 0:
                if i + 1 < m:
                    if flowerbed[i + 1] == 0 + flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i] == 1:
                        return False
                    else:
                        flowerbed[i] = 1
                        n -= 1
            elif i == m - 1:
                if i - 1 >= 0:
                    if flowerbed[i - 1] == 0 + flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i] == 1:
                        return False
                    else:
                        flowerbed[i] = 1
                        n -= 1
            else:
                if flowerbed[i] + flowerbed[i - 1] + flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        if n == 0:
            return True
        else:
            return False
