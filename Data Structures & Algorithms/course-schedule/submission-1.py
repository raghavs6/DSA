class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adjList[a].append(b)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            visit.add(i)

            for j in adjList[i]:
                if not dfs(j):
                    return False
            return True
        
        return dfs(0) and len(visit) == numCourses