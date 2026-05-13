class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while( l <= r ):
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l1, r1 = 0, len(matrix[mid]) - 1

                while(l1 <= r1):
                    mid1 = (l1 + r1) // 2

                    if matrix[mid][mid1] == target:
                        return True
                    if matrix[mid][mid1] < target:
                        l1 = mid1 + 1
                    if matrix[mid][mid1] > target:
                        r1 = mid1 - 1
                return False


            if matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False