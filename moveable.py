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
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stonesf
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up():
	'Init stones and board, prepare functions to provide, act as their closure'

#init board and game data here
	curr_player=0
	#dos llistes per evitar que ens desapareix la pedra de la tabla després de select   
	L =[] #lista de move
	Ls = [] #lista de select, len(Ls) = 8 despres de moure pedra, encara no seleccionada
	
	def stones():
		"return iterable with the stones already played"
		#Les pedres que han d'apareixer en la taula.
		return L
			
	def select_st(i,j):
		'''
		Select stone that current player intends to move. 
		Player must select a stone of his own.
		To be called only after all stones played.
		Report success by returning a boolean;
		'''		
		sel_PLAYER= Stone(x=i,y=j,color=PLAYER_COLOR[curr_player])
		if len(L) == BSIZ**2-1: 					#quan arribem a 8 pedres al tauler 
			if tuple(sel_PLAYER) in L:
				Ls.remove(tuple(sel_PLAYER))
				print("\nStone selected: ",i,j)
				return True
			else:
				print("\nERROR: Invalid position selected or the stone you want to select is not yours.")
				return False
		return True #if len(L) != BSIZ**2-1

		
	def end():
		'Test whether there are 3 aligned stones'
#Check Vertically
		for j in PLAYER_COLOR:
			for i in range(BSIZ):
				k = 0
				while (i,k,j) in Ls:
					k += 1
					if k == BSIZ:
						return True
#Check Horizontally
				k = 0
				while (k,i,j) in Ls:
					k += 1
					if k == BSIZ:
						return True
#Check Diagonally
			k = 0
			while (k,k,j) in Ls:
				k += 1
				if k == BSIZ:
					return True
			l,m = BSIZ-1, 0 
			while (l,m,j) in Ls:
				l -= 1
				m += 1
				if m == BSIZ:
					return True
		return False
		
	def move_st(i,j):
		'''If valid square, move there selected stone and unselect it,
		then check for end of game, then select new stone for next
		player unless all stones already played;
		if square not valid, do nothing and keep selected stone.
		Return 3 values: bool indicating whether a stone is
		already selected, current player, and boolean indicating
		the end of the game.
		'''
		nonlocal curr_player, select_st, L, Ls
#casos desfavorables
			
	#si coordenades equivocades	
	
		if i < 0 or i > (BSIZ-1) or j < 0 or j > (BSIZ-1):
			print("\nERROR: Maybe the input's format was wrong.")
			return (True,curr_player,end())
	
	#si coloca on ja hi ha
	
		for k in PLAYER_COLOR:	
			if (i,j,k) in L: #len(Ls) != BSIZ**2-1
				print("\nERROR: You can't put a stone over the others.")
				return (True, curr_player, end())
				
#casos favorables 

		mov_PLAYER = Stone(x=i,y=j,color=PLAYER_COLOR[curr_player])		
				
	#Player 0
		if curr_player == 0:
			Ls.append(tuple(mov_PLAYER)) 					#afegir la pedra a la Llista Ls
			L= Ls[:] 									#L fa un copia de la llista Ls
			print("\nBlue/X Stone moved to: ", i,j) 					#escriure al terminal
			curr_player = 1								#cambia de jugador
			if len(Ls)== (BSIZ**2-1) and not end():				#si hi ha vuit al tauler
				print("\nSelect a stone.")				#escriure al terminal
				select_st = False						#funció select es fals
				
	#player 1
		elif curr_player == 1:
			Ls.append(tuple(mov_PLAYER))					#afegir la pedra a la Llista Ls
			L=Ls[:]										#L fa un copia de la llista Ls
			print("\nRed/O Stone moved to: ", i,j)						#escriure al terminal
			curr_player = 0								#cambia de jugador
			if len(Ls)== (BSIZ**2-1) and not end():				#si hi ha vuit al tauler
				print("\nSelect a stone.")				#escriure al terminal
				select_st = False						#funció select es fals
				
		return (select_st, curr_player, end())	

							
	def draw_txt(end=False):
		#Dibuixar la llista
		Llista1=[] #La llista amb " " i "|"
		Llista2=[] #La llista amb "-"
		taula=[]  #La llista que imprimim, amb els símbols
		
		Llista1= (BSIZ-1)*([" "]+["|"]) + [" "]
		Llista2= ((BSIZ*2)-1)*["-"]
		
		for i in range(BSIZ):	
			taula.append (Llista1[:])
			taula.append (Llista2[:])
		taula.append(Llista1[:])
		
		def board():
			for i in range((BSIZ*2)-1):
				print(*taula[i])
				
		#Dibuixar la tabla sempre quan hi ha un canvi a la llista L
		for i in L:
			if i[2] == PLAYER_COLOR[0]:
				taula[2*(i[1])][2*(i[0])] = 'X'
			elif i[2] == PLAYER_COLOR[1]:
				taula[2*(i[1])][2*(i[0])] = 'O'
				
		board()
		
		if end:
			if curr_player == 1:
				print("\nCongratulations to 'X' player!")
			else:
				print("\nCongratulations to 'O' player!")
		else:
			if curr_player == 0:
				print('\nTHE "X" PLAYER\'S ROUND:')
			else:
				print('\nTHE "O" PLAYER\'S ROUND:')
		
		'Use ASCII characters to draw the board.'
	# return these 4 functions to make them available to the main program
	return stones, select_st, move_st, draw_txt



