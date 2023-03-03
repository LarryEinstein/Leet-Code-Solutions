#16threeSumClosest

# class Solution:
# 	def threeSumClosest(self, nums: list([int]), target: int) -> int:
# 		length = len(nums)
# 		sortedlist = sorted(nums)
# 		possible_sums = []
# 		for count, value in enumerate(sortedlist):
# 			print(count, value)
# 		# for i in range(sortedlist):
# 		# 	for j in range(1, sortedlist)

# mysolution = Solution()
# a69 = mysolution.threeSumClosest([1, 3, 6, 2, 5, 13, 12], 11)


malist = [3, 2, 8, 1]
sortedmalist = sorted(malist)
# for count, value in enumerate(sortedmalist):
# 	print(count, value)
for index, value in enumerate(sortedmalist, start=0):
	print(index, value)
for index, value in enumerate(sortedmalist, start=1):
	print(index, value)