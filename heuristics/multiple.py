from game.game2048 import Game2048

class MultipleHeuristic:
    def evaluate(self, temp_game: Game2048):
        """Combine multiple cost functions"""
        cost = 0
        
        # factor for empty tiles
        board = temp_game.board
        c_empty = sum(1 for row in board for cell in row if cell != 0)

        # factor for score
        c_score = -temp_game._score

        # factor for descending
        c_descending = 0
        # indexes = [0,1,2,3,7,6,5,4,8,9,10,11,15,14,13,12]
        # # temp_game._print_board()
        # for i,n in enumerate(indexes):
        #     if i < 15:
        #         r = n//4
        #         c = n%4
        #         next = indexes[i+1]
        #         r_next = next//4
        #         c_next = next%4
                
        #         # print(f'first tile value: {temp_game.board[r][c]}; Next tile value: {temp_game.board[r_next][c_next]}')
        #         if temp_game.board[r][c] < temp_game.board[r_next][c_next]:
        #             if temp_game.board[r_next][c_next] >=16:
        #                 c_descending += temp_game.board[r_next][c_next]

        c_snake = 0
        indexes = [0,1,2,3,7,6,5,4,8,9,10,11,15,14,13,12]
        for i,n in enumerate(indexes):
            r = n//4
            c = n%4
            for j in range(0,i):
                r_next = j//4
                c_next = j%4
                if temp_game.board[r][c] != 0:
                    if temp_game.board[r][c] > temp_game.board[r_next][c_next]:
                        c_snake += temp_game.board[r][c]

        return c_empty + c_score + c_descending + c_snake
