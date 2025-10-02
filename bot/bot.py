
from heuristics.heuristic import Heuristic
from game.game2048 import Game2048

class Bot:
    def __init__(self, heuristic: Heuristic):
        self.heuristic = heuristic

    def set_heuristic(self, heuristic: Heuristic):
        """Switch the bot's heuristic."""
        self.heuristic = heuristic

    def choose_move(self, game: Game2048, depth = 1):
        """Simulate all possible moves and return the best one."""
        moves = ['w', 'a', 'd', 's']
        best_move = None
        lowest_cost = float('inf')
        for move in moves:
            # Create a copy of the game state
            temp_game = Game2048()
            temp_game.board = [row[:] for row in game.board]
            temp_game.move_input = move
            # temp_game._print_board()
            
            # Execute the move
            if temp_game._execute_move():
                cost = self.heuristic.evaluate(temp_game)
                # print(f'Move: {move}; Cost: {cost}')
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_move = move
        
        return best_move
    def recursive_choose_move(self, game: Game2048, depth = 0):
        """Same as choose move but has depth"""
        # print(f'in recursive choose move')
        moves = ['w', 'a', 'd', 's']
        best_move = None
        lowest_cost = float('inf')
        for move in moves:
            # print(f'Move: {move}')
            # Create a copy of the game state
            temp_game = Game2048()
            temp_game.board = [row[:] for row in game.board]
            temp_game.move_input = move

            # Execute the move
            if temp_game._execute_move():
                # print(f'executed move: {move}')
                cost = self.get_cost(temp_game,depth)
                # print(f'cost of move {move}: {cost}')
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_move = move

        return best_move
        
    def get_cost(self,game: Game2048, depth):
        cost = self.heuristic.evaluate(game)
        if depth == 0:
            return cost 
        else:
            moves = ['w', 'a', 'd', 's']
            costs = []
            for move in moves:
                # Create a copy of the game state
                temp_game = Game2048()
                temp_game.board = [row[:] for row in game.board]
                temp_game.move_input = move

                # Execute the move
                if temp_game._execute_move():
                    temp_game._new_tile()
                    costs.append(self.get_cost(temp_game,depth-1))
                
            if len(costs):
                return min(costs)
            else:
                return float('inf')