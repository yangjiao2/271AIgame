# Yang Jiao 8222745. Lab assignment 4.
WHITE = 'w'
BLACK = 'b'
EMPTY = ' '
import math

def InvalidMove(Exception):
    pass

def GameOverError(Exception):
    pass

def _require_game_is_not_over(turn, cols, rows, board):
    if _game_is_over(turn, cols, rows, board):
        raise GameOverError()
    
def _require_position_is_a_valid_move(turn, cols, rows, board, pos):
    if not _is_a_valid_move(turn, cols, rows, board, pos):
        raise InvalidMove()


Direction = [(0,1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]

def _is_an_even_number_between_4_and_16(n) ->bool:
    '''check the input if the input is an even interger between 4 and 16'''
    return type(n) == int and n%2 == 0 and 4<= n <= 16

def _opposite_turn(turn)->str:
    '''Given the player whose turn it is now, returns the opposite player'''
    if turn == WHITE:
        return BLACK
    elif turn == BLACK:
        return WHITE
    
def _get_new_board(turn, cols, rows, top_left_color):
    '''generate the initial game board'''
    board =[]
    for col in range (cols):
        board.append([])
        for row in range (rows):
            board[col].append(EMPTY)
    top_right_color = _opposite_turn(top_left_color)
    board[(cols // 2) - 1][(rows // 2) - 1] = top_left_color
    board[(cols // 2) -1][(rows // 2) ] = top_right_color
    board[(cols // 2)][(rows // 2) - 1] = top_right_color
    board[(cols // 2)][(rows // 2)] = top_left_color
    return board
    
def _is_in_the_board(cols, rows, col, row):
    '''check if (col, row) is in the board)'''
    return (0<=col <cols) and (0<=row < rows)

def _color_for_a_cell(board, cols, rows, pos) -> str:
    ''' determine the color in the cell'''
    col = pos[0]
    row = pos[1]
    if _is_in_the_board(cols, rows, col, row):
        return board[col][row]
    else:
        return 'outside'

def _directions_which_near_an_opposite_turn(turn, cols, rows, board, pos) -> list:
    '''return the initial Directions where nears an opposite turn, returns a list of Directions'''
    _require_game_is_not_over(turn, cols, rows, board)
    _require_position_is_a_valid_move(turn, cols, rows, board, pos)
    
    DirList = []
    col = pos[0]
    row = pos[1]
    for i in range(8):
        if _color_for_a_cell(board, cols, rows, (col + Direction[i][0], row + Direction[i][1])) == _opposite_turn(turn):
            DirList.append((Direction[i][0], Direction[i][1]))
    return DirList
    
def _nearest_position_which_contains_same_turn(turn, cols, rows, board, pos) -> list:
    '''return the closest position where has the same color turn'''
    _require_game_is_not_over(turn, cols, rows, board)
    _require_position_is_a_valid_move(turn, cols, rows, board, pos)
    
    DirList = (_directions_which_near_an_opposite_turn(turn, cols, rows, board, pos))
    PosList = [(0,0)] * len(DirList)
    col = pos[0]
    row = pos[1]
    for i in range(len(DirList)):
        for space in range(max(cols, rows),1, -1):
            close_pos = (0,0)
            if  _color_for_a_cell(board, cols, rows, (col + DirList[i][0] * space, row + DirList[i][1] * space)) == turn:                
                PosList[i] = ((col + DirList[i][0] * space, row + DirList[i][1] * space))
                
            elif _color_for_a_cell(board, cols, rows, (col + DirList[i][0] * space, row + DirList[i][1] * space)) == EMPTY:
                PosList[i] = (0,0)
        print (PosList)
    return PosList

def _flip_pieces_in_one_direction(turn, begin_pos, direction, end_pos, board) -> list:
    '''flip all the pieces in the given direction from begin_pos to end_pos'''
    col = begin_pos[0]
    row = begin_pos[1]
    if end_pos != (0,0):
        for i in range(1, max(abs(begin_pos[0] - end_pos[0]),abs(begin_pos[1] - end_pos[1])) , 1):
            board[col + (direction[0] * i)][row + (direction[1] * i)] = turn
    return board
        
def _flip_pieces(turn, cols, rows, board, pos) -> list:
    '''flip all the pieces in all the directions which nears an opposite turn'''
    _require_game_is_not_over(turn, cols, rows, board)
    _require_position_is_a_valid_move(turn, cols, rows, board, pos)    
    
    DirList = _directions_which_near_an_opposite_turn(turn, cols, rows, board, pos)
    PosList = _nearest_position_which_contains_same_turn(turn, cols, rows, board, pos)
    print (DirList)
    print (PosList)
    for i in range(len(DirList)):
        board = _flip_pieces_in_one_direction(turn, pos, DirList[i], PosList[i], board)
    return board

def _is_a_valid_move(turn, cols, rows, board, pos) -> bool:
    '''
    check if the move is valid: 
    1. the place where the disc locates exist and is empty
    2. there is one or more than one directions has the same color as this move
    '''
    col = pos[0]
    row = pos[1]
    if board[col][row] == EMPTY:
        PosList = _nearest_position_which_contains_same_turn(turn, cols, rows, board, pos)
        print ('check  _is_a_valid_move', PosList)
        move_valid = False
        for coordinate in PosList:
            if coordinate != ((0,0)):
                move_valid = True
    else:
        move_valid = False
    return move_valid


def _no_valid_move_on_the_board(turn, cols, rows, board):
    '''check whether there exist an valid move on the board for the turn color'''
    no_valid_move = True
    for c in range(cols):
        for r in range (rows):
            if _is_a_valid_move(turn, cols, rows, board, (c,r)):
                no_valid_move = False
    return  no_valid_move
            
def _full_of_discs_on_the_board(turn, cols, rows, board):
    '''check whether the board is full of dics'''
    no_empty_cell = True
    for c in range(cols):
        for r in range (rows):
            if _color_for_a_cell(board, cols, rows, (c, r)) == ' ':
                no_empty_cell = False
    return no_empty_cell
            
def _game_is_over(turn, cols, rows, board) -> bool:
    '''check if the game is over:
    1. no valid move for both players
    2. the disc is full
    '''
    if _full_of_discs_on_the_board(turn, cols, rows, board):
        return True
    elif _no_valid_move_on_the_board(turn, cols, rows, board):
        if _no_valid_move_on_the_board((_opposite_turn(turn)), cols, rows, board):
            return False
        else:
            return True
  
def place_a_disc(turn, cols, rows, board, pos)->list:
    '''place the turn's disc, returns the board'''
    col = pos[0]
    row = pos[1]
    board[col][row] = turn
    board = _flip_pieces(turn, cols, rows, board, pos)
    return board

def print_turn(turn):
    '''print whoes turn '''
    if turn == BLACK:
        print ('It\'s Black\'s turn.')
    elif turn == WHITE:
        print ('It\'s White\'s turn.')

winning_choice = ("Two choices for winning the game\n" +
                  "1.with the most discs on the board\n"+
                  "2.with the fewest discs on the board \n")   
def _get_winning_rule():
    '''ask user to input the rule number'''
    while True:
        result = input(winning_choice)
        try:
            if (1<= int(result) <= 2):
                return int(result)
        except:
            print ('Please input 1 or 2.')

def user_friendly_board(board, cols, rows) -> list:
    '''create user friendly board by change BLACK to 'X', WHITE to 'O', EMPTY to ' '.'''
    better_board = []
    for c in range(cols):
        better_board.append([])
        for r in range(rows):
            if board[c][r] == BLACK:
                better_board[c] +=('X')
            elif board[c][r] == WHITE:
                better_board[c] +=('O')
            else:
                better_board[c]+=(' ')
    return better_board

def counter(board, cols, rows) -> str:
    '''count the number of BLACK and White dics on the board, return as a dictionary'''
    BCounter = 0
    WCounter = 0
    for c in range(cols):
        for r in range(rows):
            if board[c][r] == BLACK:
                BCounter +=1
            elif board[c][r] == WHITE:
                WCounter +=1 
    return {'b':BCounter, 'w':WCounter }

def print_board_and_information(board, cols, rows) -> str:
    '''print the board in the console'''
    index = '  '
    for i in range(rows):
        index += ' '+ ('{:2}'.format(i+1))
    bound = '   ' + '-' *  (len(index) - 2)
    print (index + '\n' + bound)
    board2 = user_friendly_board(board, cols, rows)
    for c in range(cols):
        a_line =''
        for r in range(rows):
            a_line += ' '+ ('{:2}'.format(board2[c][r]))
        print ('{:2}{}{}{:<2}'.format(c + 1, '|'+  a_line, '|',c + 1))
    print (bound+ '\n' + index + '\n')
    Dcounter = counter(board, cols, rows)
    print ('Black: ' + str(Dcounter['b']) + '\tWhite:' +str(Dcounter['w']))
    
def choose_the_winner(turn, cols, rows, board, rule):
    '''choose which one (or both player), is (are) the winner (winners)'''
    print_board_and_information(board, cols, rows)
    Dcounter = counter(board, cols, rows)
    if rule == 1:
        if Dcounter['b'] > Dcounter['w']:
            winner = 'Black'
        elif Dcounter['b'] < Dcounter['w']:
            winner = 'White'
        else:
            winner = 'Both Black and White'
    elif rule == 2:
        if Dcounter['b'] < Dcounter['w']:
            winner = 'Black'
        elif Dcounter['b'] > Dcounter['w']:
            winner = 'White'
        else:
            winner = 'Both Black and White'
    return winner