class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        

        for word in words:
            cur = root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word

        ROW, COL = len(board), len(board[0])
        res = []
        path = set()
        def dfs(r, c, node):
            

            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in path):
                return 
            letter = board[r][c]
            if letter not in node.children:
                return
            node = node.children[letter]

            if node.word is not None:
                res.append(node.word)
                node.word = None
            path.add((r,c))


            
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            path.remove((r,c))

        for i in range(ROW):
            for j in range(COL):
                dfs(i, j, root)
        return res

                    





                
