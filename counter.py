"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""
#PER GUANYAR S'HAN D'ALINEAR 5 PEDRES, SIGUI QUIN SIGUI LA MIDA DE LA TAULA

# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, WHITE, BLUISH, REDDISH

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up():
	'Init stones and board, prepare functions to provide, act as their closure'
	# init board and game data here
	L = []
	curr_player = 0
    
	def stones():
		"return iterable with the stones already played"
		return L	
		
	def select_st(i, j):
		'''
		Select stone that current player intends to move. 
		Player must select a stone of his own.
		To be called only after all stones played.
		Report success by returning a boolean;
		'''
		return True
	
	def counter():
		counter1, counter2 = 0, 0
#Check Vertically
		for j in PLAYER_COLOR:
			for i in range(BSIZ):
				k = 0 
				while k < BSIZ:
					if (i,k,j) in L  and (i,k+1,j) in L and (i,k+2,j) in L:
						if j == BLUISH:
							counter1 += 1
						else:
							counter2 += 1
					k += 1
#Check Horizontally
				k = 0 
				while k < BSIZ:
					if (k,i,j) in L  and (k+1,i,j) in L and (k+2,i,j) in L:
						if j == BLUISH:
							counter1 += 1
						else:
							counter2 += 1
					k += 1
#Check Diagonally
				for h in range(BSIZ):
					if (i,h,j) in L  and (i+1,h+1,j) in L and (i+2,h+2,j) in L:
						if j == BLUISH:
							counter1 += 1
						else:
							counter2 += 1
					if (i,h,j) in L  and (i-1,h+1,j) in L and (i-2,h+2,j) in L:
						if j == BLUISH:
							counter1 += 1
						else:
							counter2 += 1
		return (counter1, counter2)
		
	def end():
		if len(L) == BSIZ**2-1:
			if counter()[0] > counter()[1]:
				print("\nCongratulations to 'X'/BLUE player!")
			elif counter()[0] < counter()[1]:
				print("\nCongratulations to 'O'/RED player!")
			else:
				print("\nIt's a tie!")
				
			return True

		return False

	def move_st(i, j):
		'''
		If valid square, move there selected stone and unselect it,
		then check for end of game, then select new stone for next
		player unless all stones already played;
		if square not valid, do nothing and keep selected stone.
		Return 3 values: bool indicating whether a stone is
		already selected, current player, and boolean indicating
		the end of the game.
		'''
		nonlocal curr_player
		#INPUT OUT OF RANGE
		if i < 0 or i > (BSIZ-1) or j < 0 or j > (BSIZ-1):
			print("\nERROR: Maybe the input's format was wrong.")
			return (select_st,curr_player,end())
		#STONE OVER THE OTHERS
		for k in PLAYER_COLOR:	
			if (i,j,k) in L:
				print("\nERROR: You can't put a stone over the others.")
				return (select_st, curr_player, end())
				
		if curr_player == 0:
			PLAYER0 = Stone(x=i,y=j,color=PLAYER_COLOR[0])
			L.append(tuple(PLAYER0))
			curr_player = 1

		elif curr_player == 1:
			PLAYER1 = Stone(x=i,y=j,color=PLAYER_COLOR[1])
			L.append(tuple(PLAYER1))
			curr_player = 0
			
		print("\n'X'/BLUE player: ", counter()[0], "points")
		print("'O'/RED player: ", counter()[1], "points")
			
		return (select_st,curr_player, end())    
			
	def draw_txt(end=False):
        #Dibuixar la llista
		Llista1=[]
		Llista2=[]
		taula=[]
		Llista1= (BSIZ-1)*([" "]+["|"]) + [" "]
		Llista2= ((BSIZ*2)-1)*["-"]
		for i in range(BSIZ):	
			taula.append (Llista1[:])
			taula.append (Llista2[:])
		taula.append(Llista1[:])
		
		def board():
			for i in range((BSIZ*2)-1):
				print(*taula[i])
		#Posar els s¨ªmbols a la taula si hi ha canvis
		for i in L:
			if i[2] == PLAYER_COLOR[0]:
				taula[2*(i[1])][2*(i[0])] = 'X'
			elif i[2] == PLAYER_COLOR[1]:
				taula[2*(i[1])][2*(i[0])] = 'O'
				
		board()

		#Quin jugador toca posar la pedra
		if not end: 
			if curr_player == 0:
				print('\nTHE "X" PLAYER\'S ROUND:')
			else:
				print('\nTHE "O" PLAYER\'S ROUND:')
	# return these 4 functions to make them available to the main program
	return stones, select_st, move_st, draw_txt, counter
