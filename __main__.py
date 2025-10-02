import time

from game.game2048 import Game2048
from bot.bot import Bot
from heuristics.max_tile import MaxTileHeuristic
from heuristics.empty_spaces import EmptySpacesHeuristic
from heuristics.smoothness import SmoothnessHeuristic
from heuristics.wads import WadsHeuristic
from heuristics.score import ScoreHeuristic
from heuristics.descending import DescendingHeuristic
from heuristics.multiple import MultipleHeuristic

def test_heuristics(num_tests,depth):
    average_scores = []
    max_scores = []
    max_highest_tile = []
    # heuristics = [MaxTileHeuristic(), EmptySpacesHeuristic(), SmoothnessHeuristic(), WadsHeuristic(), ScoreHeuristic(),
    #               DescendingHeuristic(), MultipleHeuristic()]
    heuristics = [SmoothnessHeuristic()]
    for heuristic in heuristics:
        scores = []
        highest_tiles = []
        for n in range(num_tests):
            game = Game2048()
            bot = Bot(heuristic)
            
            while not game._is_game_over():
                move = bot.recursive_choose_move(game,depth)
                if move:
                    game.move_input = move
                    game._execute_move()
                    game._new_tile()
                    game._print_board()
                else:
                    game._print_board()
                    print(f'Game over! Game number: {n+1}')
                    break
            scores.append(game._score)
            highest_tiles.append(max(max(row) for row in game.board))
        average_scores.append(sum(scores)/num_tests)
        max_scores.append(max(scores))
        max_highest_tile.append(max(highest_tiles))

    print(f'average scores: {average_scores}')
    print(f'max scores: {max_scores}')
    print(f'max highest tiles: {max_highest_tile}')
            




def choose_heuristic():
    print("Choose a heuristic:")
    print("1. Max Tile")
    print("2. Empty Spaces")
    print("3. Smoothness")
    print("4. Wads")
    print("5. Score")
    print("6. Descending")
    print("7. Multiple")
    choice = input("Enter choice: ")

    if choice == "1":
        return MaxTileHeuristic()
    elif choice == "2":
        return EmptySpacesHeuristic()
    elif choice == "3":
        return SmoothnessHeuristic()
    elif choice == "4":
        return WadsHeuristic()
    elif choice == "5":
        return ScoreHeuristic()
    elif choice == "6":
        return DescendingHeuristic()
    elif choice == "7":
        return MultipleHeuristic()
    else:
        print("Invalid choice. Defaulting to Max Tile.")
        return MaxTileHeuristic()

if __name__ == "__main__":
    game = Game2048()
    depth = 2
    test_heuristics(1,depth)
    # heuristic = choose_heuristic()
    # bot = Bot(heuristic)
    

    # while not game._is_game_over():
    #     game._print_score()
    #     game._print_board()
    #     # move = bot.choose_move(game)
    #     move = bot.recursive_choose_move(game,depth)
    #     if move:
    #         print(f"Bot chooses: {move}")
    #         time.sleep(1)
    #         game.move_input = move
    #         game._execute_move()
    #         game._new_tile()
    #     else:
    #         print("No valid moves left. Game over!")
    #         break
    # game._print_score()
    # game._print_board()
