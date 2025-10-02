from .heuristic import Heuristic

class WadsHeuristic(Heuristic):
    "Should just prioritize moves in the order defined in bot.py: w, a, d, s"
    def evaluate(self, temp_game):
        return 1
