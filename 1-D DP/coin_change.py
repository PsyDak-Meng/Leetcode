"""
    Coin Change
    Solved 
    You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

    Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

    You may assume that you have an unlimited number of each coin.

    Example 1:

    Input: coins = [1,5,10], amount = 12

    Output: 3
    Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

    Example 2:

    Input: coins = [2], amount = 3

    Output: -1
    Explanation: The amount of 3 cannot be made up with coins of 2.

    Example 3:

    Input: coins = [1], amount = 0

    Output: 0
    Explanation: Choosing 0 coins is a valid way to make up 0.

    Constraints:

    1 <= coins.length <= 10
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10000


    Recommended Time & Space Complexity
    You should aim for a solution with O(n * t) time and O(t) space, where n is the number of coins and t is the given amount.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Keep track of the minimum combination to reach position i
        # min combination is min previous combination +1

        if amount == 0:
            return 0
        
        # Initialization: min way ot get to num is num itself
        dp = [0] * (amount+1) # need extra 0 index for initialization
        for num in coins:
            if num <= amount:
                dp[num] = 1
        
        for i in range(1, amount+1): # loop from 1 to amount
            combination_counts = []
            if dp[i] != 0: # skip if is initil coin cmount
                continue
            for num in coins: # check each coin additive combination
                prev = i-num
                if prev>=0 and dp[prev]!=0: # if previous i could not be composed, dead path
                    combination_counts.append(dp[prev]+1)
            if len(combination_counts) != 0:
                dp[i] = min(combination_counts)
        
        if dp[-1] == 0:
            return -1
        else:
            return dp[-1]
                
                
