class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        visited = set()
        path = set()
        preMap = {}

        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
                
            
            path.add(crs)


            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            path.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return res

                

