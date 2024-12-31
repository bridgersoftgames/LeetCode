s = "()]"
class Solution:
    def isValid(self, s: str) -> bool:
        for x in s:
            if x == "(":
                return ")" in s
            else:
                return False
            if x == "[":
                return "]" in s
            else:
                return False
            if x == "{":
                return "}" in s
            else:
                return False    
solution = Solution()
ans = solution.isValid(s)
print(ans)