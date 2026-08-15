class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            
            left_size = mid - in_start
            
            root.left = helper(pre_start + 1, in_start, mid - 1)
            root.right = helper(pre_start + 1 + left_size, mid + 1, in_end)
            return root
            
        return helper(0, 0, len(inorder) - 1)