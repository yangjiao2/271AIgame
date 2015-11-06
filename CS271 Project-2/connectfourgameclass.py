# connectfourgameclass.py


'''
This class is a module for implementations in the connectfour game.
'''

'''
pieces are represented by ' ', '1', '-1'

'''

NONE = ' '
PLAYER1 = '1'
PLAYER2 = '-1'


class InvalidConnectFourMoveError(Exception):
    pass

class ConnectFourGame:
    
    def _init_(self, board_col, board_row, win_len = 4):
        global NONE, PLAYER1, PLAYER2
        self.BOARD_COLUMNS = board_col
        self.BOARD_ROWS = board_row
        self.WINNING_LENGTH = win_length
        self.turn = PLAYER1
        self.winner = NONE
        self.board = self._new_game_board()

    def _new_game_board():
        global NONE, PLAYER1, PLAYER2
        self.board = []
        for col in range(self.BOARD_COLUMNS):
            self.board.append([])
            for row in range(self.BOARD_ROWS):
                self.board[-1].append(NONE)
        return self.board


    def _move_col_check(col):
        if type(col) != int or not 0 <= col < self.BOARD_COLUMNS:
            raise ValueError('column number must be int between 0 and {}'.format(self.BOARD_COLUMNS - 1))

    def _winner_check():
        global NONE, PLAYER1, PLAYER2
        if winning_player() != NONE:
            return True
        
def drop_piece(column_number):
    _move_col_check(column_number)
    empty_row = self._find_empty_row_number_in_column(column_number)

    if empty_row == -1:
        raise InvalidConnectFourMoveError()
    else:
        self.board[column_number][empty_row] = self.turn
        self._opposite_turn()


def pop_piece(column_number):
    global NONE, PLAYER1, PLAYER2
    _move_col_check(column_number)
    if self.turn == self.board[column_number][self.BOARD_ROWS - 1]:
        for row in range(self.BOARD_ROWS-1, -1, -1):
            self.board[column_number][row] = self.board[column_number][row - 1]
        self.board[column_number][row] = NONE
    self._opposite_turn()
    else:
        raise InvalidConnectFourMoveError()


def winning_player():
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


def _find_empty_row_number_in_column(column_number):
    global NONE, PLAYER1, PLAYER2   
    for i in range(self.BOARD_ROWS - 1, -1, -1):
        if self.board[column_number][i] == NONE:
            return i
    return -1



def _opposite_turn():
    global PLAYER1, PLAYER2
    if self.turn == PLAYER1:
        self.turn = PLAYER2
    else:
        self.turn == PLAYER1



def _winning_sequence_begins_at(col, row):
    return self._check_sequence_in_a_row(col, row, 0, 1) \
            or self._check_sequence_in_a_row(col, row, 1, 1) \
            or self._check_sequence_in_a_row(col, row, 1, 0) \
            or self._check_sequence_in_a_row(col, row, 1, -1) \
            or self._check_sequence_in_a_row(col, row, 0, -1) \
            or self._check_sequence_in_a_row(col, row, -1, -1) \
            or self._check_sequence_in_a_row(col, row, -1, 0) \
            or self._check_sequence_in_a_row(col, row, -1, 1)
    


def _check_sequence_in_a_row(col, row, coldelta, rowdelta):
    global NONE, PLAYER1, PLAYER2
    start_cell = self.board[col][row]
    if start_cell == NONE: 
        return False
    else:
        for i in range(1, self.WINNING_LENGTH):
            if not 0 <= col + coldelta * i < self.BOARD_COLUMNS \
                    or not 0 <= row + rowdelta * i < self.BOARD_ROWS \
                    or self.board[col + coldelta *i][row + rowdelta * i] != start_cell:
                return False
        return True
    



