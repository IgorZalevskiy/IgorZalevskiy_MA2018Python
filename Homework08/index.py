"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 20    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

PLAYERX = provided.PLAYERX #2
PLAYERO = provided.PLAYERO #3
DRAW = provided.DRAW #4
EMPTY = provided.EMPTY #1

# Add your functions here.

def mc_trial(board, player):
    """
    Runs a random trial of the game
    """
    
    while board.check_win() == None:    
        
        empty_squares = board.get_empty_squares() 
        
        random_choice = random.choice(empty_squares)
        board.move(random_choice[0],random_choice[1],player)    
            
        provided.switch_player(player) 
    
def mc_update_scores(scores, board, player):
    """
    Continually updates the scores while mc_trial runs in order to determine the best move
    """
    if board.check_win() == DRAW:
        for dummy_score in scores:
            pass 
  
    else:
        dimension = board.get_dim()
        for dummy_row in range(dimension):
            for dummy_col in range(dimension):
                
                square_status = board.square(dummy_row, dummy_col)
                           
                if square_status == EMPTY:
                    scores[dummy_row][dummy_col] += 0
                    
                elif board.check_win() == player:                
                    if square_status == player:
                        scores[dummy_row][dummy_col] += MCMATCH
                    else:
                        scores[dummy_row][dummy_col] += -MCOTHER
                        
                else:
                    if square_status == player:
                        scores[dummy_row][dummy_col] += -MCMATCH
                    else:
                        scores[dummy_row][dummy_col] += MCOTHER 
                        
def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores
    Finds all empty squares with the maximum score and
    randomly returns one of them as a (row, column) tuple
    Don't call this function with a full board
    """
    empty_tuples = board.get_empty_squares()
    
    if empty_tuples == None:
        pass
    else:
        square_scores = {}
        max_squares = []
        
        for dummy_tuple in empty_tuples:
            row = dummy_tuple[0]
            col = dummy_tuple[1]
            square_scores[dummy_tuple] = scores[row][col]
        max_score = max(square_scores.values())
        for dummy_tuple, dummy_score in square_scores.items():
            if dummy_score == max_score:
                max_squares.append(dummy_tuple)
        random_max_square = random.choice(max_squares)
        return random_max_square



def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is,
    and the number of trials to run
    Uses the Monte Carlo simulation to return a move for the
    machine player in the form of a (row, column) tuple
    Use these functions already defined:
        mc_trial(board, player)
        mc_update_scores(scores, board, player)
        get_best_move(board, scores)
    """
    
    trial_board = board.clone()

    dim = board.get_dim()

    scores = [[0 for dummy_col in range(dim)] for dummy_row in range(dim)]
    
    for dummy_trial in range(trials):
        mc_trial(trial_board, player)

        mc_update_scores(scores, trial_board, player)
        
        trial_board = board.clone()
            
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)