from collections import defaultdict
class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if (board[r][c] in rows[r] or \
                        board[r][c] in cols[c] or \
                        board[r][c] in box[(r//3, c//3)]):
                        return False
                    
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    box[(r//3, c//3)].add(board[r][c])
                
        return True

boards = map(loads, stdin)
f = open('user.out', 'w')
for board in boards:
    result = Solution.isValidSudoku(board)
    print('true' if result else 'false', file=f)
