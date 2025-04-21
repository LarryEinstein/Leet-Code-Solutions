# python/7reverseInteger.py
class Solution:
    def reverse(self, x: int) -> int:
        
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        # recall sequence: [start:stop:step]
        x = str(x)
        length_x = len(x)
        print(f"length_x is {length_x}")
        x = x[::-1]
        output = sign * int(x)

        # Check for 32-bit integer overflow
        if output >= 2**31 - 1 or output <= -2**31:
            return 0
        return output

# Example usage
a1 = Solution()
print(a1.reverse(123))   # Output: 321
print(a1.reverse(-123))  # Output: -321
print(a1.reverse(120))   # Output: 21