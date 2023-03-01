#3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == target:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum<target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        print(output)

mysolution = Solution()
a1 = mysolution.threeSum(nums = [-1,0,1,2,-1,-4])
