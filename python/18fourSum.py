from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, result = len(nums), []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1; right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

# Test cases
case1nums = [1, 0, -1, 0, -2, 2]
case1target = 0
case2nums = [2, 2, 2, 2, 2]
case2target = 8

case1Solution = Solution()
result1 = case1Solution.fourSum(case1nums, case1target)
print(f"Case 1 result: {result1}")

case2Solution = Solution()
result2 = case2Solution.fourSum(case2nums, case2target)
print(f"Case 2 result: {result2}")