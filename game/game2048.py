import random

class Game2048:

    def __init__(self):
        self.board = [[0]*4, [0]*4, [0]*4, [0]*4]

        # Start with 2 random tiles filled in
        self._new_tile()
        self._new_tile()

        self._score = 0
        self._game_over = False

    def play_bot(self):
        """Play the game with the bot making moves."""
        while not self._game_over:
            self._print_score()
            self._print_board()

            # Bot chooses a move
            valid_moves = ["w", "a", "s", "d"]
            best_move = self._choose_best_move(valid_moves)
            self.move_input = best_move

            # Execute the move
            moved = self._execute_move()
            if not moved:
                print("Invalid move chosen by bot.")
                continue

            self._new_tile()
            if self._is_game_over():
                self._game_over = True

        print("Game Over!")
        self._print_score()
        self._print_board()

    def play_human(self):
        """Play the game with a human making moves."""
        while not self._game_over:
            self._print_score()
            self._print_board()
            moved = False
            while not moved:
                self._get_move_input()
                moved = self._execute_move()
            self._new_tile()

            if self._is_game_over():
                self._game_over = True

        print("Game Over!")
        self._print_score()
        self._print_board()

    def _is_game_over(self):
        """Check if there are no valid moves left."""
        for move in ["w", "a", "s", "d"]:
            board_copy = [row[:] for row in self.board]
            self.move_input = move
            if self._execute_move():
                self.board = board_copy
                return False
        return True

    def _print_score(self):
        print(f'Score: {self._score}')

    def _print_board(self):
        """display board to terminal
        Could be improved for having different length numbers"""

        print('_'*20)
        for r in range(4):
            row_str = "|"
            for c in range(4):
                row_str += ' '
                row_str += str(self.board[r][c])
                row_str += ' |'
            print(row_str)
            print('_'*20)   

    def _get_move_input(self):
        self.move_input = input("Input move: ")         

    def _index_to_rc(self,index):
        """index to row and column"""
        return (index//4,index%4)
    
    def _rc_to_index(self,r,c):
        """"row and column to index"""
        return 4*r+c

    def _new_tile(self):
        """Adds either a 2 or 4 to an empty space
        Assuming there is an empty space to find"""
        # print("new_tile")
        possible_indexes = []

        # Find the empty spaces
        for r in range(4):
            for c in range(4):
                if self.board[r][c] == 0:
                    possible_indexes.append(self._rc_to_index(r,c))

        try:
            chosen_index = random.choice(possible_indexes)
            (row,column) = self._index_to_rc(chosen_index)
            # print(f'chosen index: {chosen_index}; row: {row}; column: {column}')
            self.board[row][column] = random.choice([2, 4])
        except:
            print("Tried to add tile to full board. Error!")

    def _execute_move(self):
        """Executes input move. returns True if the board changed, False if it did not."""
        moved = False
        if self.move_input == "a":
            moved = self._move_left()
        elif self.move_input == "d":
            moved = self._move_right()
        elif self.move_input == "w":
            moved = self._move_up()
        elif self.move_input == "s":
            moved = self._move_down()
        else:
            print("Invalid move")

        return moved

    def _move_left(self):
        # print("move left")
        moved = False

        # Loop over rows
        for r in range(4):
            #To keep track of what has been seen already going left to right
            first_empty = -1
            last_full = -1
            last_full_merged = False

            #Loop over columns
            for c in range(4):
                # print(f'row: {r}; column: {c}; first empty: {first_empty}; last_full: {last_full}')

                # If tile empty
                if self.board[r][c] == 0:
                    # print("empty")
                    # If it's the first empty tile we have seen, save the column index
                    if first_empty < 0: #Empty
                        # print("first empty")
                        first_empty = c

                # Tile contains a number
                else:
                    # This tile should merge with the tile to the left of it
                    if last_full >= 0 and self.board[r][last_full] == self.board[r][c] and not last_full_merged:
                        # print("merge")
                        self.board[r][last_full] *= 2
                        self._score+=self.board[r][last_full]
                        self.board[r][c] = 0
                        last_full_merged = True
                        if first_empty <= 0:
                            first_empty = c
                        moved = True
                            
                    # This tile should slide as far left as possible
                    elif first_empty >= 0:
                        # print("slide all the way left")
                        self.board[r][first_empty] = self.board[r][c]
                        self.board[r][c] = 0
                        last_full = first_empty
                        first_empty += 1
                        moved = True
                        last_full_merged = False
                    
                    # This full tile shouldn't move, just update that we've seen a more recent full tile
                    else:
                        # print("update last full")
                        last_full = c
                        last_full_merged = False
        return moved

    def _move_right(self):
        # print("move right")
        moved = False

        # Loop over rows
        for r in range(4):
            #To keep track of what has been seen already going right to left
            first_empty = -1
            last_full = -1
            last_full_merged = False

            #Loop over columns
            for c in range(3,-1,-1):
                # print(f'row: {r}; column: {c}; first empty: {first_empty}; last_full: {last_full}')

                # If tile empty
                if self.board[r][c] == 0:
                    # print("empty")
                    # If it's the first empty tile we have seen, save the column index
                    if first_empty < 0: #Empty
                        # print("first empty")
                        first_empty = c

                # Tile contains a number
                else:
                    # This tile should merge with the tile to the right of it
                    if last_full >= 0 and self.board[r][last_full] == self.board[r][c] and not last_full_merged:
                        # print("merge")
                        self.board[r][last_full] *= 2
                        self._score+=self.board[r][last_full]
                        self.board[r][c] = 0
                        last_full_merged = True
                        if first_empty <= 0:
                            first_empty = c
                        moved = True
                            
                    # This tile should slide as far right as possible
                    elif first_empty >= 0:
                        # print("slide all the way right")
                        self.board[r][first_empty] = self.board[r][c]
                        self.board[r][c] = 0
                        last_full = first_empty
                        first_empty -= 1
                        moved = True
                        last_full_merged = False
                    
                    # This full tile shouldn't move, just update that we've seen a more recent full tile
                    else:
                        # print("update last full")
                        last_full = c
                        last_full_merged = False



        return moved

    def _move_up(self):
        # print("move up")
        moved = False

        # Loop over columns left to right
        for c in range(4):
            #To keep track of what has been seen already going right to left
            first_empty = -1
            last_full = -1
            last_full_merged = False

            # Loop over rows top to bottom
            for r in range(4):
                # If tile empty
                if self.board[r][c] == 0:
                    # print("empty")
                    # If it's the first empty tile we have seen, save the row index
                    if first_empty < 0:
                        # print("first empty")
                        first_empty = r

                # Tile contains a number
                else:
                    # This tile should merge with the tile above it
                    if last_full >= 0 and self.board[last_full][c] == self.board[r][c] and not last_full_merged:
                        # print("merge")
                        self.board[last_full][c] *= 2
                        self._score+=self.board[last_full][c]
                        self.board[r][c] = 0
                        last_full_merged = True
                        if first_empty <= 0:
                            first_empty = r
                        moved = True
                            
                    # This tile should slide as far up as possible
                    elif first_empty >= 0:
                        # print("slide all the way right")
                        self.board[first_empty][c] = self.board[r][c]
                        self.board[r][c] = 0
                        last_full = first_empty
                        first_empty += 1
                        moved = True
                        last_full_merged = False
                    
                    # This full tile shouldn't move, just update that we've seen a more recent full tile
                    else:
                        # print("update last full")
                        last_full = r
                        last_full_merged = False

        return moved
    
    def _move_down(self):
        # print("move down")
        moved = False
        
        # Loop over columns left to right
        for c in range(4):
            #To keep track of what has been seen already going right to left
            first_empty = -1
            last_full = -1
            last_full_merged = False

            # Loop over rows bottom to top
            for r in range(3,-1,-1):
                # If tile empty
                if self.board[r][c] == 0:
                    # print("empty")
                    # If it's the first empty tile we have seen, save the row index
                    if first_empty < 0:
                        # print("first empty")
                        first_empty = r

                # Tile contains a number
                else:
                    # This tile should merge with the tile above it
                    if last_full >= 0 and self.board[last_full][c] == self.board[r][c] and not last_full_merged:
                        # print("merge")
                        self.board[last_full][c] *= 2
                        self._score+=self.board[last_full][c]
                        self.board[r][c] = 0
                        last_full_merged = True
                        if first_empty <= 0:
                            first_empty = r
                        moved = True
                            
                    # This tile should slide as far up as possible
                    elif first_empty >= 0:
                        # print("slide all the way right")
                        self.board[first_empty][c] = self.board[r][c]
                        self.board[r][c] = 0
                        last_full = first_empty
                        first_empty -= 1
                        moved = True
                        last_full_merged = False
                    
                    # This full tile shouldn't move, just update that we've seen a more recent full tile
                    else:
                        # print("update last full")
                        last_full = r
                        last_full_merged = False

        return moved