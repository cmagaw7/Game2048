from .heuristic import Heuristic

class ChuckHeuristic(Heuristic):
    """Custom heurictic"""
    def evaluate(self, temp_game):
        board = temp_game.board
        score = 0
        for r in range(4):
            for c in range(4):
                if r < 3 and c < 3:
                    if board[r][c] >= board[r][c+1]: score += board[r][c]
                    if board[r][c] >= board[r+1][c]: score += board[r][c]
                # print(f"row: {r}, col: {c}, board: {board[r][c]}")
        return score
