from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        def is_strictly_increasing(arr, start, end):
            for i in range(start, end):
                if arr[i] >= arr[i+1]:
                    return False
            return True

        for a in range(n - 2 * k + 1):
            b = a + k
            if is_strictly_increasing(nums, a, a + k - 1) and is_strictly_increasing(nums, b, b + k - 1):
                return True
        return False