example_1 = "23"
example_2 = ""
example_3 = "2"


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        letter_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            for char in letter_map[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res

sol1 = Solution()
result1 = sol1.letterCombinations(example_1)
print(result1)

sol2 = Solution()
result2 = sol2.letterCombinations(example_2)
print(result2)

sol3 = Solution()
result3 = sol3.letterCombinations(example_3)
print(result3)

