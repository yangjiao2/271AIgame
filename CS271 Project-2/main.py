import connectfourgame, smartai

NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'


if __name__ == "__main__":
	cfg = connectfourgame.connectfourgame(8,8) # 8 * 8 
	cfg.print_board()
	row = 0
	col = 3
	while(not cfg._check_winner_exist() and cfg.check_within_boundary(col, row)):
		# TODO: 
		# determine move, check if the tile is free, make move
		# below is a sample code, does only drop and print
		
		(row, col) = smartai.Ai2(cfg.board, cfg.turn).make_move()
		if (cfg.check_empty(col,row)):
			cfg.drop_piece(col,row)
			row = row + 1
			cfg.print_board()


