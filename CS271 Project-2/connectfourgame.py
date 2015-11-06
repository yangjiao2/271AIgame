'''
This class is a module for implementations in the connectfour game.
'''


NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'


class ConnectFourGame:
    
    def __init__(self, board_col, board_row, win_length):
        global NONE, PLAYER1, PLAYER2
        self.BOARD_COLUMNS = board_col
        self.BOARD_ROWS = board_row
        self.WINNING_LENGTH = win_length
        self.turn = PLAYER1
        self.winner = NONE
        self.board = self._new_game_board()

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
        if type(row) != int or not 0 <= row < self.BOARD_COLUMNS:
            raise ValueError('column number must be int between 0 and {}'.format(self.BOARD_COLUMNS - 1))

    def _check_winner_exist(self):
        global NONE, PLAYER1, PLAYER2
        if self.winning_player() != NONE:
            return True
        return False

    def check_empty(self, col, row):
        ''' check if a tile is empty, return True if it is empty; this can be used by AI to check available moves '''
        if self.board[col][row] == NONE:
            return True
        else:
            return False
            
    def drop_piece(self, column_number, row_number):
        ''' drop a piece on the board'''
        self._col_check(column_number)
        self._row_check(row_number)
 
        if (not self.check_empty(column_number, row_number)):
            raise ValueError('row ' + str(row_number) + ', column ' + str(column_number) + ' has been taken')
        else:
            self.board[column_number][row_number] = self.turn
            self._opposite_turn()

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
        return NONE

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
                        or self.board[col + coldelta *i][row + rowdelta * i] != start_cell:
                    return False
            return True
        



