#4medianOfTwoSortedArrays

class Solution(object):
	def findMedianSortedArray(nums1, nums2):
 		

		# nums1 = [1, 2, 4, 5]
		# nums2 = [3, 6, 9, 12, 13, 13, 35, 27]

		combined_array = nums1 + nums2

		print(combined_array)

		combined_array.sort()

		print(combined_array)

		print(len(combined_array))

		print(combined_array[int(0)])


		if len(combined_array)%2==0:
			value = combined_array[int((len(combined_array)-1)/2)] + combined_array[int((len(combined_array))/2)]
			median = value/2
			print(median)
		else:
			median = combined_array[int((len(combined_array)-1)/2)]
			print(median)

a1 = Solution.findMedianSortedArray(nums1 = [1, 2, 4, 5], nums2 = [3, 6, 9, 12, 13, 13, 35, 27])