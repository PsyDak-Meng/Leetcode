"""
    Find the Duplicate Number
    Solved 
    You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

    Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

    Example 1:

    Input: nums = [1,2,3,2,2]

    Output: 2
    Example 2:

    Input: nums = [1,2,3,4,4]

    Output: 4
    Follow-up: Can you solve the problem without modifying the array nums and using 
    O
    (
    1
    )
    O(1) extra space?

    Constraints:

    1 <= n <= 10000
    nums.length == n + 1
    1 <= nums[i] <= n


    Recommended Time & Space Complexity
    You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.
    """

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## Use list index as hash map 
        # ex. value of nums[i] is key and nums[abs(nums[i])] is hash set
        # it will be using the hash set's positive/negative t0 indicate whether the value of abs(nums[i]) has been seen, this is built on the 1-n integer restriction

        for i in range(len(nums)):
            # check if abs(nums[i]) has been seen by checking if it's negative
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            
            # make negative to hash has seen
            nums[abs(nums[i])] = -1 * nums[abs(nums[i])]


