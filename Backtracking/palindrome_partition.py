"""
    Palindrome Partitioning
    Solved 
    Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

    You may return the solution in any order.

    Example 1:

    Input: s = "aab"

    Output: [["a","a","b"],["aa","b"]]
    Example 2:

    Input: s = "a"

    Output: [["a"]]
    Constraints:

    1 <= s.length <= 20
    s contains only lowercase English letters.


    Recommended Time & Space Complexity
    You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the length of the input string.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindromic(string):
            return string == string[::-1]
        
        # DFS: traverse each idx [partition/not]
        # SubTree: keep track of idx and current partition, sub traverse
        def dfs(i, cur):
            # has made sure palindromic, if current partition is full, add to result
            length = 0
            for string in cur:
                length += len(string)
                if length == len(s):
                    res.append(cur.copy())
            
            # Traverse
            for j in range(i+1, len(s)+1): # need to traverse to last one so +1
                if is_palindromic(s[i:j]):
                    cur.append(s[i:j])
                    dfs(j, cur)

                    # backtrack
                    cur.pop()
            
        dfs(0, [])
        return res
    

                
