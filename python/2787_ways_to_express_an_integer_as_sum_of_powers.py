class Solution:
    def numberOfWays(self, n, x):
        """
        Calculates the number of ways to express a number n as the sum of
        distinct numbers each raised to the power of x. This version
        uses memoization to prevent redundant calculations and improve performance.

        Args:
            n (int): The target number.
            x (int): The power to raise each number to.

        Returns:
            int: The number of ways.
        """
        
        # Determine the maximum possible base number, safely handling floating-point errors.
        max_num = int(round(n ** (1 / x)))

        # Create a list of possible base numbers from 1 up to max_num.
        possible_numbers = list(range(1, max_num + 1))
        possible_numbers.reverse()
        
        # A dictionary to store the results of solved subproblems.
        # The key is a tuple (target, index) and the value is the number of ways.
        memo = {}

        # The recursive helper function, now with memoization.
        def find_combinations(target, numbers, power, index=0):
            # Check if this subproblem has already been solved.
            if (target, index) in memo:
                return memo[(target, index)]

            # Base Case 1: Found a solution.
            if target == 0:
                return 1

            # Base Case 2: Went too far or out of numbers.
            if target < 0 or index >= len(numbers):
                return 0

            # Choice 1: Include the current number.
            count_with_current = find_combinations(target - (numbers[index] ** power), numbers, power, index + 1)

            # Choice 2: Exclude the current number.
            count_without_current = find_combinations(target, numbers, power, index + 1)

            # Store the result in the memoization table before returning.
            result = count_with_current + count_without_current
            memo[(target, index)] = result
            return result

        if not possible_numbers:
            return 0
        
        return find_combinations(n, possible_numbers, x)


# --- Example Usage ---
# Create an instance of the Solution class.
solution = Solution()

# Test with n = 10, x = 2.
# The expected result is 1 (3^2 + 1^2).
target_number = 10
power_x = 2
ways = solution.numberOfWays(target_number, power_x)
print(f"Target n={target_number}, Power x={power_x}")
print(f"Number of ways: {ways}")

print("\n--- Another Example ---")
# Test with n = 100, x = 2.
# The expected result is 9, e.g. (10^2), (8^2 + 6^2), etc.
target_number_2 = 100
power_x_2 = 2
ways_2 = solution.numberOfWays(target_number_2, power_x_2)
print(f"Target n={target_number_2}, Power x={power_x_2}")
print(f"Number of ways: {ways_2}")

print("\n--- Time Limit Test Case ---")
# Test with n = 90, x = 1. This is a common test case that requires optimization.
target_number_3 = 90
power_x_3 = 1
ways_3 = solution.numberOfWays(target_number_3, power_x_3)
print(f"Target n={target_number_3}, Power x={power_x_3}")
print(f"Number of ways: {ways_3}")
