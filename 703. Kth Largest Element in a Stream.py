class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = map(lambda x:-x, nums)
        self.nums = sorted(list(nums))[:k]

    def add(self, val: int) -> int:
        bisect.insort(self.nums, -val)
        if len(self.nums) > self.k:
            self.nums.pop()
        return -self.nums[-1]