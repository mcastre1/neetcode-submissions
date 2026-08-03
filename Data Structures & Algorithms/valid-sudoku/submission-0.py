class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows:
        for row in board:
            seen = {}
            for n in row:
                if n in seen and n != '.':
                    return False
                else:
                    seen[n] = 1
        
        # Columns:
        for i in range(9):
            seen = {}
            for j in range(9):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                else:
                    seen[board[j][i]] = 1

        # Squares
        for blockRow in range(3):
            for blockColumn in range(3):
                seen = {}
                for i in range(3):
                    for j in range(3):
                        val = board[(blockRow * 3) + i][(blockColumn * 3) + j]
                        if val in seen and val != '.':
                            return False
                        seen[val] = 1

        return True