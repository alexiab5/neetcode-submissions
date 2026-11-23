class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        rows, cols = len(board), len(board[0])

        class TrieNode:
            def __init__(self):
                self.children = {}  # char -> TrieNode
                self.word = None    # full word at end of path

        # 1. Build Trie from target words
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        result = []

        # 2. Backtrack on board, guided by Trie
        def dfs(r: int, c: int, parent: TrieNode) -> None:
            ch = board[r][c]
            curr = parent.children.get(ch)
            if curr is None:
                return

            if curr.word is not None:
                result.append(curr.word)
                curr.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, curr)
            board[r][c] = ch  # restore cell

            # Optional optimization: prune leaf nodes that no longer hold words
            if not curr.children and curr.word is None:
                parent.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result