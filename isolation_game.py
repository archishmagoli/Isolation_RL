class Grid(object):

    # Defines the parameters for the Grid object
    def __init__(self, player_1, player_2, height=3, width=3):
        self.player_1 = player_1
        self.player_2  = player_2
        self.width = width # 3x3 grid currently
        self.height = height
        self.active_player = player_1 # Player whose turn it currently is
        self.inactive_player = player_2 # Opposing player
        self.move_count = 0

    # Determines if proposed move is legal based on current location of player in grid
    def is_legal_move():
        if 1 == 1: # Conditions TBD based on gameplay
            return True
        else:
            return False
    
    # Hand over turn to opposing player once turn has been completed
    def make_move(self, move):
        self._active_player, self._inactive_player = self._inactive_player, self._active_player
        self.move_count += 1
    
    # Evaluate current board state to determine winner (if any)
    def evaluate_board_state():
        return True # TBD based on gameplay
    
    def get_possible_moves(self, current_location):
        possible_moves = [current_location] # Possible moves dependent on current location
        return possible_moves
    
