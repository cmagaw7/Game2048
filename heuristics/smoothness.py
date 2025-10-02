from .heuristic import Heuristic

class SmoothnessHeuristic(Heuristic):
    """ChatGPT created, not really sure what it's trying to do"""
    def evaluate(self, temp_game):
        board = temp_game.board
        smoothness = 0
        for r in range(4):
            for c in range(4):
                if c < 3 and board[r][c] > 0:
                    smoothness -= abs(board[r][c] - board[r][c + 1])
                if r < 3 and board[r][c] > 0:
                    smoothness -= abs(board[r][c] - board[r + 1][c])
        return -smoothness
