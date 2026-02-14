class Solution():
    def main(self, nums, p):
        print(f"nums are {nums}")
        print(f"p is {p}")

        dict_of_checked_subarray_indices = {}

        sum_nums = sum(nums)

        count_of_elements_removed = 0
        if sum_nums % p == 0:
            return 0
        elif sum_nums % p != 0:
            print(f"current distance from modulo 0 is {sum_nums % p}")
            for i in range(len(nums)-1):
                if nums[i] == p:
                    return 1
        else:
            return 0

a1 = Solution()
a1.main(nums=[3,1,4,2], p=6)

new_nums = [4, 8, 1, 3]
new_nums_sorted = sorted(new_nums)
print(new_nums_sorted)