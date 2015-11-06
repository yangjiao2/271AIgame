import ConnectFourGame

if __name__ == "__main__":
	cfg = ConnectFourGame.ConnectFourGame(8,8) # 8 * 8 
	cfg.print_board()
	row = 0
	
	while(not cfg._check_winner_exist() and row < cfg.BOARD_ROWS):
                # TODO: 
		# determine move, check if the tile is free, make move
		# below is a sample code, does only drop and print
		cfg.drop_piece(3,row)
		row = row + 1
		cfg.print_board()


