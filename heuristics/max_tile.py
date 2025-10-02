from .heuristic import Heuristic

class MaxTileHeuristic(Heuristic):
    """Pick move that creates the largest tile in number"""
    def evaluate(self, temp_game):
        board = temp_game.board
        return -max(max(row) for row in board)
