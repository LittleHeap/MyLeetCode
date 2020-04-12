class Solution:
    def insert(self, A: List[List[int]], B: List[int]) -> List[List[int]]:

        index = bisect.bisect_left(A, B)

        if index > 0:
            if B[0] <= A[index - 1][1]:
                A[index - 1][1] = max(B[1], A[index - 1][1])
                while index < len(A) and A[index - 1][1] >= A[index][0]:
                    A[index - 1][1] = max(A[index][1], A[index - 1][1])
                    A.pop(index)
                return A

        A.insert(index, B)
        while index + 1 < len(A) and A[index][1] >= A[index + 1][0]:
            A[index][1] = max(A[index + 1][1], A[index][1])
            A.pop(index + 1)
        return A

