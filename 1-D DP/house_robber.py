"""
    House Robber
    Solved 
    You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

    You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

    Return the maximum amount of money you can rob without alerting the police.

    Example 1:

    Input: nums = [1,1,3,3]

    Output: 4
    Explanation: nums[0] + nums[2] = 1 + 3 = 4.

    Example 2:

    Input: nums = [2,9,8,3,6]

    Output: 16
    Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

    Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100


    Recommended Time & Space Complexity
    You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of houses.
    """

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialization
        n = len(nums)
        dp = [0] * n

        # 1. shor edge case, limit=2
        if n<3:
            return max(nums)
        # 2. max reward at idx is the larger of reward at idx-1/idx-2 + reward at i (cuz not rob adjacent)
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]


