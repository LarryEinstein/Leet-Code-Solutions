from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results: List[str] = []
        def backtrack(path: str, open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                results.append(path)
                return
            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return results