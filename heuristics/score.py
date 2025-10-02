from .heuristic import Heuristic
from game.game2048 import Game2048

class ScoreHeuristic(Heuristic):
    """Choose moves that increases the score the most"""
    def evaluate(self, temp_game: Game2048):
        return -temp_game._score