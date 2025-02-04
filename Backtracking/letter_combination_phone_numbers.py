"""
    Letter Combinations of a Phone Number
    Solved 
    You are given a string digits made up of digits from 2 through 9 inclusive.

    Each digit (not including 1) is mapped to a set of characters as shown below:

    A digit could represent any one of the characters it maps to.

    Return all possible letter combinations that digits could represent. You may return the answer in any order.



    Example 1:

    Input: digits = "34"

    Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
    Example 2:

    Input: digits = ""

    Output: []
    Constraints:

    0 <= digits.length <= 4
    2 <= digits[i] <= 9


    Recommended Time & Space Complexity
    You should aim for a solution with O(n * (4^n)) time and O(n) space, where n is the length of the input string.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur):
            if i==len(digits):
                print(i, cur)
                res.append(cur)
                return 
            for char in digitToChar[digits[i]]:
                cur += char
                dfs(i+1, cur)
                # backtrack
                cur = cur[:-1]
        
        dfs(0, "")
        return res


                
