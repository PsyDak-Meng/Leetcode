"""
    Combination Sum II
    Solved 
    You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

    Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

    You may return the combinations in any order and the order of the numbers in each combination can be in any order.

    Example 1:

    Input: candidates = [9,2,2,4,6,1,5], target = 8

    Output: [
    [1,2,5],
    [2,2,4],
    [2,6]
    ]
    Example 2:

    Input: candidates = [1,2,3,4,5], target = 7

    Output: [
    [1,2,4],
    [2,5],
    [3,4]
    ]
    Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30


    Recommended Time & Space Complexity
    You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        # DFS: keep track of current combination & backtrack using index pointer
        def dfs(i:int, cur, total:int):
        # Substructure: sorted, then each new node traversed determine same problem in right hand sub tree
            nonlocal res, candidates

            # match -> end path (all candidates on the right are too large)
            if total == target:
                res.append(cur.copy()) # modifying cur inplace, use deep copy
                return
            # exceed target -> end path (all candidates on the right are too large)
            if total > target or i==len(candidates):
                return 
            
            # not exceed target，add candidate & traverse right candidates
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            # backtrack
            cur.pop()
            # skip duplicates within range
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i += 1
            # explore right subtree after backtracked
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)

        return res
                
