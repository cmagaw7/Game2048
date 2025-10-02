import random

class Board2:
    def __init__(self):
        self.board = [[0]*4, [0]*4, [0]*4, [0]*4]
        self._score = 0

        self.moves = 0

        # Start with 2 random tiles filled in
        self.new_tile()
        self.new_tile()

    def copy(self):
        board_copy = Board2()
        board_copy.board = #### finish here?

    def move(self, move):
        print(f"move in board2.move: {move}")
        moved = False
        if move == "a":
            moved = self._move_left()
        elif move == "d":
            moved = self._move_right()
        elif move == "w":
            moved = self._move_up()
        elif move == "s":
            moved = self._move_down()
        else:
            print("Invalid move")

        return moved
    
    def _index_to_rc(self,index):
        """index to row and column"""
        return (index//4,index%4)
    
    def _rc_to_index(self,r,c):
        """"row and column to index"""
        return 4*r+c

    def new_tile(self):
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

    def print(self):
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

    
    def print_score(self):
        print(f'Score: {self._score}')

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