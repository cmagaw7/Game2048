import random
from heuristics.heuristic import Heuristic
from game2.board2 import Board2

class Game2:

    def __init__(self, heuristic: Heuristic):
        # self.board = [[0]*4, [0]*4, [0]*4, [0]*4]

        # # Start with 2 random tiles filled in
        # self._new_tile()
        # self._new_tile()
        self.board = Board2()

        self.heuristic = heuristic

        self._game_over = False

    # def get_best_move(self):
    #     best_move = "w"
    #     for move in ["w", "a", "s", "d"]:
    #         board_copy = [row[:] for row in self.board]
    #         self.move_input = move
    #         if self._execute_move():
    #             self.board = board_copy
    #             return False
    #     return True


    def get_value(self):
        return self.heuristic.evaluate(self.board)

    def play_bot(self):
        """Play the game with the bot making moves."""
        pass

    def play_human(self):
        """Play the game with a human making moves."""
        while not self._game_over:
            self.board.print_score()
            print(f"cost: {self.get_value()}")
            self.board.print()
            moved = False
            while not moved:
                move = self._get_move_input()
                print(f"move: {move}; board after move:")
                moved = self.board.move(move)
                self.board.print()
            self.board.new_tile()

            if self._is_game_over():
                self._game_over = True

        print("Game Over!")
        self.board.print_score()
        self.board.print()

    def _is_game_over(self):
        """Check if there are no valid moves left."""
        for move in ["w", "a", "s", "d"]:
            print(f"checking game over; move: {move}")
            self.board.print()
            temp_board = self.board # Issue with copying!!!!!!!!!!
            if temp_board.move(move):
                return False
            print("temp")
            temp_board.print()
        return True

    def _get_move_input(self):
        return input("Input move: ")         