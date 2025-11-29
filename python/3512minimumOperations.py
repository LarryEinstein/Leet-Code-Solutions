class Solution():
    # def main(self, nums, k):
    #     current_sum = sum(nums)
    #     number_of_operations = 0

    #     print(f"current sum is {current_sum}")
    #     print(f"k is {k}")
    #     if current_sum < k:
    #         return False
    #     print(current_sum % k)
    #     # while current_sum % k

    #     return number_of_operations
    
    # took me a shameful amount of code to realise
    # this was do-able in 11 characters

    def get_number_of_operations(self, nums, k):
        return sum(nums) % k


nums, k = [3, 9, 7], 5

a1 = Solution()

print(a1.get_number_of_operations(nums, k))