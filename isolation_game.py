class Grid(object):

    BLANK = '_'
    NOT_MOVED = None

    # Defines the parameters for the Grid object
    def __init__(self, player_1, player_2, height=3, width=3):
        self.player_1 = player_1
        self.player_2  = player_2
        self.width = width # 3x3 grid currently
        self.height = height
        self.active_player = player_1 # Player whose turn it currently is
        self.inactive_player = player_2 # Opposing player
        self.move_count = 0

        self.grid = init_grid(self)

    # Creates initial grid for players    
    def init_grid(self):
        grid = {}


        return grid
    
    # Grid property
    @property
    def grid(self):
        return self._grid
    
    # Active player property
    @property
    def active_player(self):
        return self._active_player

    # Inactive player property
    @property
    def inactive_player(self):
        return self._inactive_player

    # Determines if proposed move is legal based on current location of player in grid
    def is_legal_move(self, move):
        if 1 == 1: # Conditions TBD based on gameplay
            # If move coordinate is in the the legel_moves array
            return True
        else:
            return False
        
    # Get list of legal moves
    def get_legal_moves(self, player=None):
        if (player == None):
            player = self.active_player
        
        legal_moves = []

        return legal_moves
    
    # Get blank spaces after each turn
    def get_blank_spaces(self):
        blank_spaces = []
        return blank_spaces

    # Returns string representation of board
    def print_board():
        board_string = ""
        return board_string

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

    def play_game():
        winner_present = False

        # Repeated until winner_present is true
            # List of legal moves generated for Player 1
            # Player 1 makes move
            # Hashmap is updated
            # List of legal moves generated for Player 2
            # Player 2 makes move

        return True # Outlines gameplay for this grid
    
