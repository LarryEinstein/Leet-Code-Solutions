class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        s=float('inf')
        t=len(nums)
        nums.sort()
        for x in range(t-2):
            i=x+1
            j=t-1
            while i<j:
                s1=nums[x]+nums[i]+nums[j]
                #print(x,i,j,'here')
                if s1==target:
                    return target
                if abs(target-s)>abs(target-s1):
                    #print(x,i,j,'-------',s1)
                    s=s1
                if s1<target:
                    i+=1
                else:
                    j-=1
        print(s)

mysolution = Solution()
a69 = mysolution.threeSumClosest([1, 2, 4, 1, 21, 4, 8, 5, 1, 9, 7, 8], 22)
print(a69)