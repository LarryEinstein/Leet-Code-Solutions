from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        max_k = 0
        
        def is_strictly_increasing(arr, start, end):
            for i in range(start, end):
                if arr[i] >= arr[i+1]:
                    return False
            return True
        
        # Try all possible values of k from 1 to n//2
        for k in range(1, n // 2 + 1):
            found = False
            # Check all possible starting positions for the first subarray
            for a in range(n - 2 * k + 1):
                b = a + k
                if (is_strictly_increasing(nums, a, a + k - 1) and 
                    is_strictly_increasing(nums, b, b + k - 1)):
                    found = True
                    break
            if found:
                max_k = k
        
        return max_k

a1 = Solution()
print(a1.maxIncreasingSubarrays(nums=[2,5,7,8,9,2,3,4,3,1]))