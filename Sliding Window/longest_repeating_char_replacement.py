# Longest Repeating Character Replacement
"""
    You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

    Example 1:

    Input: s = "XYYX", k = 2

    Output: 4
    Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

    Example 2:

    Input: s = "AAABABB", k = 1

    Output: 5
    Constraints:

    1 <= s.length <= 1000
    0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            Sol:

            1. Imagin a window r at each char, l from the beginning,
            this window goes to a current char in str and add count 1 for this current counts.     
            The count here represents your window, they are the count of chars inthe l:r window.

            Keep track of the max original consecutive streak inside the window, max_c.

            2. (r-l+1) is the  full extent, and max_c is the max original consecutive streak without allowed k replacement.
            If current char strecthes beyond k, shift window right till it does not go beyond k replacement and update counts.

            3. Update longest extent after making sure satisdies k replacement.
        """

        max_c = 0
        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1 # add consec count to the current char
            max_c = max(max_c, count[s[r]]) # keep track of the max consec count inside the window

            while (r-l+1)-max_c > k: # window extended beyond k replacements
                count[s[l]] -= 1 # subtract the consec counts & shift right untill satisfy k
                l += 1
            
            res = max(res, r-l+1) # keep track of max length
        
        return res