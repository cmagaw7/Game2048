from game2.game2 import Game2
from heuristics.chuck import ChuckHeuristic

if __name__ == "__main__":

    heuristic = ChuckHeuristic()
    game = Game2(heuristic)
    game.play_human()

