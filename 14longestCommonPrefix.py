#14longestCommonPrefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest_str = min(strs, key=len)

        # Loop through each character in the shortest string
        for i, char in enumerate(shortest_str):
            # Check if the character is the same in all strings
            for other_str in strs:
                if other_str[i] != char:
                    # If the characters don't match, return the prefix up to this point
                    return shortest_str[:i]

        # If we've made it through the loop, all strings have the same prefix
        return shortest_str

strs = ["hello", "hell", "helicopter", "help"]

mysolution=Solution()

a69 = mysolution.longestCommonPrefix(strs)

print(a69)