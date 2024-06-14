def reset_pos():
	while get_pos_x() > 0:
		move(West)
		
	while get_pos_y() > 0:
		move(South)
	
reset_pos()