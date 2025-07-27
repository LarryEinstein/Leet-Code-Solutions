class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string is valid.
        
        Args:
            s: String containing only '(', ')', '{', '}', '[' and ']'
            
        Returns:
            True if the string is valid, False otherwise
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary mapping closing brackets to their corresponding opening brackets
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
                # print(f"stack: {stack}")
            # If it's a closing bracket
            elif char in ')}]':
                # If stack is empty, there's no matching opening bracket
                if not stack:
                    return False
                
                # Check if the top of stack matches the expected opening bracket
                if stack.pop() != bracket_pairs[char]:
                    return False
        
        # After processing all characters, stack should be empty
        return len(stack) == 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((", False),
        ("))", False),
        ("({[]})", True),
        ("(((", False),
        (")))", False)
    ]
    
    for test_input, expected in test_cases:
        result = solution.isValid(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{test_input}' -> {result} (Expected: {expected})") 