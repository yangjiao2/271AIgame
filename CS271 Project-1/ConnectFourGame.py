'''
This class is a module for implementations in the connectfour game.
'''


# from Gui import NONE, PLAYER1, PLAYER2
#import SmartAiModule
from SmartAiModule import BasicAi, AdvAi, TrueAlphaAi, RandomAi

NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'


class ConnectFourGame:
    
    def __init__(self, board_col, board_row, mode, win_length=4):
        global NONE, PLAYER1, PLAYER2
        self.BOARD_COLUMNS = board_col
        self.BOARD_ROWS = board_row
        self.WINNING_LENGTH = win_length
        self.turn = PLAYER1
        self.winner = NONE
        self.board = self._new_game_board()
        self.firstMove = True
        self.mode = mode
        self.moveindex = 1
        #===========================================================
        # Input AI here?
        #===========================================================
        if mode == 2:
            self.ai = BasicAi(PLAYER2, self.board, len(self.board), self.firstMove)
        if mode == 3:
            self.firstMove1 = True
            self.ai1 = AdvAi(PLAYER1, self.board, len(self.board), self.firstMove1)
            #self.ai1 = TrueAlphaAi(PLAYER1, self.board, len(self.board), self.firstMove1)
            self.firstMove2 = True 
            self.ai2 = BasicAi(PLAYER2, self.board, len(self.board), self.firstMove2)
            #self.ai2 = RandomAi(PLAYER1, self.board, len(self.board), self.firstMove2)

    def _new_game_board(self):
        global NONE, PLAYER1, PLAYER2
        self.board = []
        for col in range(self.BOARD_COLUMNS):
            self.board.append([])
            for row in range(self.BOARD_ROWS):
                self.board[-1].append(NONE)
        return self.board


    def _col_check(self, col):
        if type(col) != int or not 0 <= col < self.BOARD_COLUMNS:
            raise ValueError('column number must be int between 0 and {}'.format(self.BOARD_COLUMNS - 1))

    def _row_check(self, row):
        if type(row) != int or not 0 <= row < self.BOARD_ROWS:
            raise ValueError('column number must be int between 0 and {}'.format(self.BOARD_COLUMNS - 1))

    def check_winner_exist(self):
        global NONE, PLAYER1, PLAYER2
        if self.winning_player() != NONE:
            return True
        return False
    
    def check_within_boundary(self, col, row):
        return 0 <= col < self.BOARD_COLUMNS and 0 <= row < self.BOARD_ROWS

    def check_empty(self, col, row):
        ''' check if a tile is empty, return True if it is empty; this can be used by AI to check available moves '''
        if self.board[col][row] == NONE:
            return True
        else:
            return False
    
    def turn(self):
        global NONE, PLAYER1, PLAYER2
        if (self.turn == NONE):
            return "NONE"
        elif (self.turn == PLAYER1):
            return "PLAYER1"
        else:
            return "PLAYER2"

    def drop_piece_without_ai(self, column_number, row_number):
        global NONE, PLAYER1, PLAYER2
        self._col_check(column_number)
        self._row_check(row_number)
        if (not self.check_empty(column_number, row_number)):
            raise ValueError('row ' + str(row_number) + ', column ' + str(column_number) + ' has been taken')

        self.board[column_number][row_number] = self.turn
        self._opposite_turn()
        self.moveindex = self.moveindex + 1

        
    def drop_piece(self, column_number=None, row_number=None):
        ''' drop a piece on the board'''
        global NONE, PLAYER1, PLAYER2
        if (column_number != None and row_number != None):
            if (not self.check_empty(column_number, row_number)):
                raise ValueError('row ' + str(row_number) + ', column ' + str(column_number) + ' has been taken')
        if self.mode == 1:
            self.drop_piece_without_ai(column_number, row_number)
        elif self.mode == 2:
            if (self.moveindex % 2):
                self.drop_piece_without_ai(column_number, row_number)
            else:
                (row, col) = self.ai.make_move(self.board, len(self.board))
                self.drop_piece_without_ai(col, row)
                self.firstMove = False
        elif self.mode == 3:
            if (self.moveindex % 2):
                (row, col) = self.ai1.make_move(self.board, len(self.board))
                self.drop_piece_without_ai(col, row)
                self.firstMove1 = False
            else:
                (row, col) = self.ai2.make_move(self.board, len(self.board))
                self.drop_piece_without_ai(col, row)
                self.firstMove2 = False


    def winning_player(self):
        ''' get winnner, if no winner, return NONE '''
        global NONE, PLAYER1, PLAYER2
        winner = NONE
        for col in range(self.BOARD_COLUMNS):
            for row in range(self.BOARD_ROWS):
                if self._winning_sequence_begins_at(col, row):
                    if winner == NONE:
                        winner = self.board[col][row]
                    else:
                        self._opposite_turn()
        self.winner = winner
        return self.winner

    def print_board(self):
        ''' print the board in console '''
        print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.board]))
        print ('\n')

    def _find_empty_row_number_in_column(self, column_number):
        global NONE, PLAYER1, PLAYER2   
        for i in range(self.BOARD_ROWS - 1, -1, -1):
            if self.board[column_number][i] == NONE:
                return i
        return -1

    def _opposite_turn(self):
        global PLAYER1, PLAYER2
        if self.turn == PLAYER1:
            self.turn = PLAYER2
            return
        else:
            self.turn = PLAYER1
            return

    def _winning_sequence_begins_at(self, col, row):
        return self._check_sequence_in_a_row(col, row, 0, 1) \
                or self._check_sequence_in_a_row(col, row, 1, 1) \
                or self._check_sequence_in_a_row(col, row, 1, 0) \
                or self._check_sequence_in_a_row(col, row, 1, -1) \
                or self._check_sequence_in_a_row(col, row, 0, -1) \
                or self._check_sequence_in_a_row(col, row, -1, -1) \
                or self._check_sequence_in_a_row(col, row, -1, 0) \
                or self._check_sequence_in_a_row(col, row, -1, 1)
        
    def _check_sequence_in_a_row(self, col, row, coldelta, rowdelta):
        global NONE, PLAYER1, PLAYER2
        start_cell = self.board[col][row]
        if start_cell == NONE: 
            return False
        else:
            for i in range(1, self.WINNING_LENGTH):
                if not 0 <= col + coldelta * i < self.BOARD_COLUMNS \
                        or not 0 <= row + rowdelta * i < self.BOARD_ROWS \
                        or self.board[col + coldelta * i][row + rowdelta * i] != start_cell:
                    return False
            return True
        



