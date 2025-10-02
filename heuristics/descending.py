from .heuristic import Heuristic
from game.game2048 import Game2048

class DescendingHeuristic(Heuristic):
    """Goal is to create a snake effect of the values of the tiles starting in the top left"""
    def evaluate(self, temp_game: Game2048):
        score = 0
        indexes = [0,1,2,3,7,6,5,4,8,9,10,11,15,14,13,12]
        for i,n in enumerate(indexes):
            if i < 15:
                r = n//4
                c = n%4
                next = indexes[i+1]
                r_next = next//4
                c_next = next%4
                if temp_game.board[r][c] < temp_game.board[r_next][c_next]:
                    score -= temp_game.board[r_next][c_next]
        return score

            


