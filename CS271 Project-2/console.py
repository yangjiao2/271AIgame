# Yang Jiao 8222745. Lab assignment 4.

WHITE = 'w'
BLACK = 'b'
EMPTY = ' '
import collections

import gamecode
            

greeting = "Welcome to Othello Game!\n"
ending = "Thanks for playing Othello Game. Bye!"

def _who_move_first()->str:
    '''ask user to input who move first'''
    while True:
        result = input('Who move first: Black (B) or white (W)?\n').strip().lower()
        if result == 'black' or result == 'b':
            return BLACK
        elif result == 'white' or result == 'w':
            return WHITE
        else:
            print (result + 'is not an valid answer. Please try again.')
        
def _which_color_on_top_left()->str:
    '''ask user to input the top left color'''
    while True:
        result = input('Which color located on the top left of the first four center cells? \nBlack (B) or white (W)?\n').strip().lower()
        if result == 'black' or result == 'b':
            return BLACK
        elif result == 'white' or result == 'w':
            return WHITE
        else:
            print (result + 'is not an valid answer. Please try again.')

def _get_cols()->int:
    while True:
        result = input('Please input the number of columes and rows:\nCol:')
        try:
            if gamecode._is_an_even_number_between_4_and_16(int(result)):
                return int(result)
            else:
                print (str(result) + 'is not a valid answer.')
        except:
            print (str(result) + 'is not an valid answer. Please input an even number of columes on the board between 4 and 16.')
            
def _get_rows()->int:
    while True:
        result = input('Row:')
        try:
            if gamecode._is_an_even_number_between_4_and_16(int(result)):
                return int(result)
            else:
                print (str(result) + 'is not a valid answer.')
        except:
            print (str(result) + 'is not an valid answer. Please an even number of rows on the board between 4 and 16.')

def _get_move_col(cols)->int:
    while True:
        result = input('Please input the number of columes and rows you want to input a disc:\nCol:')
        try:
            if (int(result))<=cols:
                return int(result)
            else:
                print (str(result) + 'is not a valid answer.')
        except:
            print (str(result) + 'is not a valid answer. Please input an integer')
            
def _get_move_row(rows)->int:
    while True:
        result = input('Row:')
        try:
            if (int(result))<=rows:
                return int(result)
            else:
                print (str(result) + 'is not a valid answer.')
        except:
            print (str(result) + 'is not a valid answer. Please input an integer')

winning_choice = ("Two choices for winning the game\n" +
                  "1.with the most discs on the board\n"+
                  "2.with the fewest discs on the board \n")   
def _get_winning_rule():
    while True:
        result = input(winning_choice)
        try:
            if (1<= int(result) <= 2):
                return int(result)
            else:
                print (str(result) + 'is not a valid answer.')
        except:
            print (result + ' is invalid. Please input integer 1 or 2.')
            
class Othello:

    def __init__(self, turn, cols, rows, board):
        self._turn = turn
        self._cols = cols
        self._rows = rows
        self._board = board

    def _turn(self):
        return self._turn
    
    def _col(self):
        return self._cols
    
    def _row(self):
        return self._rows
    
    def _board(self):
        return self._board

    def take_turns(self):
        while not gamecode._game_is_over(self._turn, self._cols, self._rows, self._board):
            if _no_valid_move_on_the_board(self._turn, self._cols, self._rows, self._board):
                self._turn = gamecode._opposite_turn(self._turn)
            gamecode.print_board_and_information(self._board, self._cols, self._rows)
            gamecode.print_turn(self._turn)
            col = _get_move_col(self._cols)
            row = _get_move_row(self._rows)
            pos = (col - 1, row - 1)
            while not gamecode._is_a_valid_move(self._turn, self._cols, self._rows, self._board, pos):
                board = self._board
                print (board)
                print ('The move '+ str((col, row))+' is invalid. Please try again...')
                col = _get_move_col(self._cols)
                row = _get_move_row(self._rows)
                pos = (col - 1, row - 1)
            self._board = gamecode.place_a_disc(self._turn, self._cols, self._rows, self._board, pos)
            self._turn = gamecode._opposite_turn(self._turn)

    def play_game():
        onemoretime = 'suppose_yes'
        while onemoretime:
            print (greeting)
            
            cols = _get_cols()
            rows = _get_rows()
            turn = _who_move_first()
            top_left_color =  _which_color_on_top_left()
            board = gamecode._get_new_board(turn, cols, rows, top_left_color)
            game = Othello(turn, cols, rows, board)
            rule = _get_winning_rule()
            print ('\nGame Starts!\n')
            
            Othello.take_turns(game)

            print ('\nGame Ends!\n')
            
            winner = gamecode.choose_the_winner(game._turn, game._cols, game._rows, game._board, rule)
            print ('The winner is(are): '+ winner + '\nCongratulations!')
            print ('\nThanks for playing the game. Do you want to play again?')
            onemoretime = (input('Press <ENTER> if you want to quit.\nOtherwise, press any key(s) on the keyboard.'))
        print (ending)
        
if __name__ == '__main__':

    Othello.play_game()
    
#####################################################################################################