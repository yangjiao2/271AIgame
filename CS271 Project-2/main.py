import ConnectFourGame

if __name__ == "__main__":
	cfg = ConnectFourGame.ConnectFourGame(8,8,4)
	cfg.print_board()
	row = 0
	
	while(not cfg._check_winner_exist() and row < cfg.BOARD_ROWS):
		''' determine move, check if free, make move '''
		cfg.drop_piece(3,row)
		row = row + 1
		cfg.print_board()

#endWhile
