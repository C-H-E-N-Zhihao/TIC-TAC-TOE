"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""

# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, WHITE, BLUISH, REDDISH

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player = 4):
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
		
	def end():

#Check Vertically
		for j in PLAYER_COLOR:
			for i in range(BSIZ): 
				k = 0
				while (i,k,j) in L:
					k += 1
					if k == BSIZ:
						return True
#Check Horizontally
				k = 0
				while (k,i,j) in L:
					k += 1
					if k == BSIZ:
						return True
#Check Diagonally
			k = 0
			while (k,k,j) in L:
				k += 1
				if k == BSIZ:
					return True
			l,m = BSIZ-1, 0 
			while (l,m,j) in L:
				l -= 1
				m += 1
				if m == BSIZ:
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
			return (select_st, curr_player, end())
		elif curr_player == 1:
			PLAYER1 = Stone(x=i,y=j,color=PLAYER_COLOR[1])
			L.append(tuple(PLAYER1))
			curr_player = 0
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
		#Posar els símbols a la taula si hi ha canvis
		for i in L:
			if i[2] == PLAYER_COLOR[0]:
				taula[2*(i[1])][2*(i[0])] = 'X'
			elif i[2] == PLAYER_COLOR[1]:
				taula[2*(i[1])][2*(i[0])] = 'O'
				
		board()
		#Quan gana o empateix
		if end:
			if curr_player == 1:
				print("\nCongratulations to 'O' player!")
			else:
				print("\nCongratulations to 'X' player!")
				
		if not end and len(L) == (BSIZ**2):
			print("\nIt's a tie! Write a enter to close the game")
			end = True
		else:
			if curr_player == 0:
				print('\nTHE "X" PLAYER\'S ROUND:')
			else:
				print('\nTHE "O" PLAYER\'S ROUND:')

		#Quin jugador toca posar la pedra

	# return these 4 functions to make them available to the main program
	return stones, select_st, move_st, draw_txt
