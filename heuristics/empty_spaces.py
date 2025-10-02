from .heuristic import Heuristic

class EmptySpacesHeuristic(Heuristic):
    """Pick move that results in the most empty spaces"""
    def evaluate(self, temp_game):
        board = temp_game.board
        return sum(1 for row in board for cell in row if cell != 0)
