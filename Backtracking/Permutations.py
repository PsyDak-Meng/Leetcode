"""
    Permutations
    Solved 
    Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

    Example 1:

    Input: nums = [1,2,3]

    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Example 2:

    Input: nums = [7]

    Output: [[7]]
    Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10


    Recommended Time & Space Complexity
    You should aim for a solution with O(n * n!) time and O(n) space, where n is the size of the input array.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)

        # DFS
        def dfs_permute(cur, r_nums):
        # Sub problem: each call has current combination & remaining nums
            nonlocal nums, l, res
            # if reaches combination length, kill path
            if len(cur)==l:
                res.append(cur.copy()) # modify cur inplace, use deep copy
                return
            # traverse remaining nums at this position
            for num in r_nums:
                r_nums_copy = r_nums.copy()
                cur.append(num)
                r_nums_copy.remove(num)
                dfs_permute(cur, r_nums_copy)

                # backtrack on current position
                cur.pop()
        
        dfs_permute([], nums)
        return res
                
