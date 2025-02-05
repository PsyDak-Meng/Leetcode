"""
    Longest Palindromic Substring
    Solved 
    Given a string s, return the longest substring of s that is a palindrome.

    A palindrome is a string that reads the same forward and backward.

    If there are multiple palindromic substrings that have the same length, return any one of them.

    Example 1:

    Input: s = "ababd"

    Output: "bab"
    Explanation: Both "aba" and "bab" are valid answers.

    Example 2:

    Input: s = "abbc"

    Output: "bb"
    Constraints:

    1 <= s.length <= 1000
    s contains only digits and English letters.


    Recommended Time & Space Complexity
    You should aim for a solution as good or better than O(n^2) time and O(1) space, where n is the length of the given string.
    """

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two Pointers: palindrom has to be the same from each side expanding from the middle
        # find center -> expand -> update
        # keep track of longest len and starting index
        start, max_len = 0,0

        for i in range(len(s)):
            # odd palindrom has one char centers
            l,r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:
                    start = l
                    max_len = r-l+1
                l -= 1
                r += 1

            # even palindrome has two char centers
            l,r, = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:
                    start = l
                    max_len = r-l+1
                l -= 1
                r += 1
            
        return s[start : start+max_len]

