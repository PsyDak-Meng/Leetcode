"""
    Decode Ways
    Solved 
    A string consisting of uppercase english characters can be encoded to a number using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

    "JAB" with the grouping (10 1 2)
    "JL" with the grouping (10 12)
    The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

    Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

    Example 1:

    Input: s = "12"

    Output: 2

    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
    Example 2:

    Input: s = "01"

    Output: 0
    Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

    Constraints:

    1 <= s.length <= 100
    s consists of digits


    Recommended Time & Space Complexity
    You should aim for a solution as good or better than O(n) time and O(n) space, where n is the length of the given string.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # Top-down
        dp = {len(s):1} # keep track of ways to decode string from right most
        
        # DFS explore ways to decode all right side of index i
        def dfs(i):
            # memoization
            if i in dp:
                return dp[i]
            
            # edge case: 0 can't decode
            if s[i] == "0":
                return 0
            
            # decode 1 char
            res = dfs(i+1)

            # decode 2 chars
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                res += dfs(i+2)
            
            return res
        
        return dfs(0)
    

        # Bottom-up
        dp = {len(s):1} # keep track of ways to decode string from right most

        for i in range(len(s)-1, -1,-1): # traverse ways to decode all right side of index i
            if s[i] == "0": # edge case: can't deocde 0, so ways to decode using i as a start is none
                dp[i] = 0
            else:
                dp[i] = dp[i+1] # decode 1

            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"): # decode 2
                dp[i] += dp[i+2]
            
        return dp[0]
