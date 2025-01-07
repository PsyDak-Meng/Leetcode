"""
    Permutation in String    
    Solved 
    You are given two strings s1 and s2.

    Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

    Both strings only contain lowercase letters.

    Example 1:

    Input: s1 = "abc", s2 = "lecabee"

    Output: true
    Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

    Example 2:

    Input: s1 = "abc", s2 = "lecaabee"

    Output: false
    Constraints:

    1 <= s1.length, s2.length <= 1000


    Recommended Time & Space Complexity
    You should aim for a solution with O(n) time and O(1) space, where n is the maximum of the lengths of the two strings.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Sol:

            1. Imagin a window r at each char, l from the beginning,
            this window keeps a window size same as s1.     

            2. Keep track of the count in this windo2.
            If window size over s1's, delete the left most char in window_count and remove the key if 0 count so dicts can match.
        """
        l = 0
        window_count, s1_count = {},{}
        n1 = len(s1)

        # s1 char counts
        for i in range(n1):
            s1_count[s1[i]] = s1_count.get(s1[i],0) + 1
        
        # sliding window of size s1
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r],0) + 1

            # if newly added is over s1 size
            while (r-l+1) > n1:
                # remove left most char count
                window_count[s2[l]] -= 1
                # pop left most key if it has 0 count
                if window_count[s2[l]] == 0:
                    window_count.pop(s2[l])
                l += 1
            
            if window_count==s1_count:
                return True
        
        return False

