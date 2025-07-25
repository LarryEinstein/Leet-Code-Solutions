class Solution:
    def numberOfArrays(differences, lower, upper):
        n = len(differences)
        
        # Initialize min and max values for the first element of the hidden sequence
        min_first = 0
        max_first = 0
        
        # Calculate the prefix sums to find the min and max possible values
        current_sum = 0
        for diff in differences:
            current_sum += diff
            min_first = min(min_first, current_sum)
            max_first = max(max_first, current_sum)
        
        # Calculate the valid range for the first element
        valid_min = lower - min_first
        valid_max = upper - max_first
        
        # The number of valid starting points is the overlap of the ranges
        return max(0, valid_max - valid_min + 1)

    # Example usage
    print(numberOfArrays([1, -3, 4], 1, 6))  # Output: 2
    print(numberOfArrays([3, -4, 5, 1, -2], -4, 5))  # Output: 4
    print(numberOfArrays([4, -7, 2], 3, 6))  # Output: 0
        
    

