#twoSum.py

class Solution1:
	def __init__(self, nums1, target1):
		self.nums1 = nums1
		self.target1 = target1


	def twoSum1(nums1, target1):
		length = len(nums1)
		for i in range(0, length):
			for j in range(i+1, length):
				if nums1[i] + nums1[j] == target1:
					return ([nums1[i], nums1[j]])
		return []


# a = Solution1.twoSum1([1, 2, 3, 4], 6)
# print(a)


class Solution2:
	def __init__(self, nums2, target2):
		self.nums2 = nums2
		self.target2 = target2

	def twoSum2(nums2, target2):
		matches = {}
		for number in nums2:
			match = target2 - number
			if match in matches:
				return [match, number]
			else:
				matches[number] = True
		return []

b = Solution2.twoSum2([1, 2, 3, 4], 6)
print(b)

class Solution3:
	def __init__(self, nums3, target3):
		self.nums3 = nums3
		self.target3 = target3

	def twoSum3(nums3, target3):
	    nums3.sort()
	    left = 0
	    right = len(nums3) - 1
	    while left < right:
	        if nums3[left] + nums3[right] == target3:
	            return [nums3[left], nums3[right]]
	        elif nums3[left] + nums3[right] < target3:
	            left +=1
	        elif nums3[left] + nums3[right] > target3:
	            right -=1
	    return []

# c = Solution3.twoSum3([1, 2, 3, 4], 6)
# print(c)