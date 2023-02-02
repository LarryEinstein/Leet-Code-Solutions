# #4medianOfTwoSortedArrays

# class Solution(object):
# 	def findMedianSortedArray(self, nums1, nums2):
# 		

array1 = [1, 2, 4, 5]
array2 = [3, 6, 9, 11]

combined_array = array1 + array2

print(combined_array)

combined_array.sort()

print(combined_array)

print(len(combined_array))

print(combined_array[int(0)])


if len(combined_array)%2==0:
	value = combined_array[int((len(combined_array))/2-1)] + combined_array[int((len(combined_array))/2)]
	median = value/2
	print(median)
else:
	median = combined_array[int(len(combined_array-1))]/2
	print(median)

