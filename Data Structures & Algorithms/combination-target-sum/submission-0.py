class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        path = []
        def dfs(i):
            if sum(path) == target:
                res.append(path.copy())
                return
            if sum(path) > target:
                return
            if i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(i)
            path.pop()
            dfs(i + 1)
        dfs(0)
        return res

            

            