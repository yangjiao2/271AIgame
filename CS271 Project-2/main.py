import connectfourgame


cfg = ConnectFourGame(8,8,4)
i = 0
while(cfg.winning_player == NONE):
	''' determine move, check if free, make move '''
	cfg.drop_piece(3,i)
	i = i + 1
	cfg.print_board()

#endWhile
