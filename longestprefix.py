# 14. Longest Common Prefix
# Easy
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 # Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
# Initialize the prefix with the first string 
        prefix = strs[0] 
        # Compare the prefix with each string in the list
        for string in strs[1:]: 
            
            while not string.startswith(prefix): 
            
                # Reduce the prefix length by one character at a time 
                prefix = prefix[:-1] 
            
                # If the prefix becomes empty, return an empty string 
                if not prefix: 
                    return "" 
        return prefix

#remove for leetcode IDE

'''
solution = Solution()
answer = solution.isPalindrome(x)
print(answer)
'''