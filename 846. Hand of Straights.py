class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        d = collections.Counter(hand)

        hand.sort()

        for num in hand:
            if num in d:
                d[num] -= 1
                if d[num] == 0:
                    del d[num]
            else:
                continue
            for i in range(1, W):
                if num + i in d:
                    d[num + i] -= 1
                    if d[num + i] == 0:
                        del d[num + i]
                else:
                    return False

        return True

