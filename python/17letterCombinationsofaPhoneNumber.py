# python/17letterCombinationsofaPhoneNumber

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:  # Handle empty string case
            return []
            
        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        # Initialize with first digit's letters
        result = dict[digits[0]]
        
        # For each additional digit, combine with previous results
        for digit in digits[1:]:  # Start from second digit
            temp = []  # Temporary list to store new combinations
            for prefix in result:  # For each existing combination
                for letter in dict[digit]:  # For each letter of current digit
                    temp.append(prefix + letter)  # Combine them
            result = temp  # Update result with new combinations
            
        return result

if __name__ == "__main__":
    # This code only runs when you run this file directly
    solution = Solution()
    
    # Test cases
    test_cases = [
        "23",    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        "",      # []
        "2",     # ["a","b","c"]
        "234",   # ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi",...]
    ]
    
    for digits in test_cases:
        result = solution.letterCombinations(digits)
        print(f"Input: {digits}")
        print(f"Output: {result}\n")
