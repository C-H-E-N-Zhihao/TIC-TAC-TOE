"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Pygame-based handling of a simple tic-tac-toe-like board, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
"""

# Import library for game programming 
import pygame

while True:
	mode_game=input("Select mode (Default, Counter, Moveable, Middle or Adjacent): ")
	if mode_game != "Default" and mode_game != "Counter" and mode_game != "Moveable" and mode_game != "Middle" and mode_game != "Adjacent":
		print("\nYour input is wrong. Correct input: 'Default', 'Counter', 'Moveable', 'Middle', 'Adjacent'\n")
	else:
		break
		
while True:
	if mode_game == "Counter":
		print("Counter mode selected")
		mode_win = "NOTHING"
		from counter import set_board_up
		break
	mode_win=input("Select the winning mode (Normal or Misery): ")
	if mode_win != "Normal" and mode_win != "Misery":
		print("\nYour input is wrong. Correct input: 'Normal' or 'Misery'\n")
	else: 
		break
		
if mode_win == "Normal":
	print("\nNormal mode selected")
	
	if mode_game == "Default":
		print("Default mode selected")
		from default import set_board_up
		
	elif mode_game == "Moveable" :
		print("Moveable mode selected")
		from moveable import set_board_up
		
	elif mode_game == "Middle":
		print("Middle mode selected")
		from middle import set_board_up
		
	elif mode_game == "Adjacent":
		print("Adjadent mode selected")
		from adjacent import set_board_up	

elif mode_win == "Misery":
	print("\nMisery mode selected")
	
	if mode_game == "Default":
		print("Default mode selected")
		from default_misery import set_board_up
		
	elif mode_game == "Moveable" :
		print("Moveable mode selected")
		from moveable_misery import set_board_up
		
	elif mode_game == "Middle":
		print("Middle mode selected")
		from middle_misery import set_board_up
		
	elif mode_game == "Adjacent":
		print("Adjadent mode selected")
		from adjacent_misery import set_board_up	


# Import: colors BLACK, GRAY, WHITE, PLAYER_COLOR; 
#         board dimensions BSIZ, WIDTH, HEIGHT, SLOT, SEP, ROOM, RAD
from constants import *
from math import pi
# Initialize the game engine, indicate a caption and
# set the height and width of the screen.
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Import initialization of the separately programmed abstract board:



# Prepare board:
# this will set up all stones as unplayed, select a first stone to play,
# and obtain functions to handle them as follows:
#   the call stones() allows one to loop on all stones,
#   the call select_st(i, j) marks as selected the stone at these coordinates,
#   the call move_st(i, j) 
#     if the square at these coordinates is free, moves the selected  
#     stone there, changes player, unselects the stone and checks for 
#     end of game; otherwise, does nothing, leaving the stone selected;
#     returns: bool "stone still selected", next player (may be the same), 
#     and bool "end of game"
#   the call to draw_txt(end) prints a text-based version of the board
if mode_game == "Counter":
	stones, select_st, move_st, draw_txt, counter = set_board_up()
else:
	stones, select_st, move_st, draw_txt = set_board_up()

# Grid:
def trans_coord(x, y):
	'translates pixel coordinates into board coordinates'
	return round((x - ROOM - SEP - 0.5*SLOT)/(SEP + SLOT)), round((y - SEP - 0.5*SLOT)/(SEP + SLOT))

def draw_square(screen, i, j):
	pygame.draw.polygon(screen, GRAY,
		( (ROOM + SEP + i*(SLOT + SEP), SEP + j*(SLOT + SEP)),
		(ROOM + SEP + i*(SLOT + SEP) + SLOT, SEP + j*(SLOT + SEP)),
		(ROOM + SEP + i*(SLOT + SEP) + SLOT, SEP + j*(SLOT + SEP) + SLOT),
		(ROOM + SEP + i*(SLOT + SEP), SEP + j*(SLOT + SEP) + SLOT)
		))

def draw_stone(screen, i, j, color):
	pygame.draw.circle(screen, color, 
		(ROOM + 0.5*SEP + (i + 0.5)*(SLOT + SEP), 0.5*SEP + (j + 0.5)*(SLOT + SEP)), 
		RAD)

#[(0,1,BLUISH),(0,2,BLUISH),(0,0,BLUISH)]
def draw_board(curr_player = 0, end = False):
	'on fresh screen, draw grid, stones, player turn mark, then make it appear'
	
	if not end:
		screen.fill (WHITE)
		if mode_game == "Default" and len(stones())== BSIZ**2:
			print("It is a Tie.")
			screen.fill(PURPLE)
	elif end and mode_game == "Counter":
		if counter()[0] > counter()[1]:
			screen.fill(BLUISH)
		elif counter()[0] < counter()[1]:
			screen.fill(REDDISH)
		else:
			screen.fill(PURPLE)
	else:
		if curr_player == 1 and mode_win == "Normal": #curr_player = 1, winner es BLUISH perque l'ultim move_st ho ha fet BLUISH
			print("The winner is BLUISH.")
			screen.fill(PLAYER_COLOR[0])
		elif curr_player == 0 and mode_win == "Normal":
			print("The winner is REDDISH.")
			screen.fill(PLAYER_COLOR[1])
		elif curr_player == 1 and mode_win == "Misery":
			print("The winner is REDDISH.")
			screen.fill(PLAYER_COLOR[1])
		elif curr_player == 0 and mode_win == "Misery":
			print("The winner is BLUISH.")
			screen.fill(PLAYER_COLOR[0])
	for i in range(BSIZ):
		for j in range(BSIZ):
			draw_square(screen, i, j)
	for s in stones():
		draw_stone(screen, *s)
	if not end:
		'colored rectangle indicates who plays next'
		pygame.draw.rect(screen, PLAYER_COLOR[curr_player], 
		(ROOM + SEP, BSIZ*(SEP + SLOT) + SEP, BSIZ*(SEP + SLOT) - SEP, SLOT))
	pygame.display.flip()

# set_board_up() already selects a first stone; set curr_player to zero.
stone_selected = True
curr_player = 0

# Show grid and stones:
draw_board()

# Loop until the user clicks the close button.
done = False

# Play until game ends
end = False

while not done:       #Como acabar con el juego
    
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    
    for event in pygame.event.get():              #eventos dentro del juego
        "User did something"
        if event.type == pygame.QUIT:              #cierras el juego si le das a la x
            "User clicked 'close window', set flag to exit loop"
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and not end:            #si clicas cualquier lugar del tablero 
            "game is afoot and user clicked something"
            if stone_selected:                                           #si clicas en una pieza
                "User should click on a free destination square, otherwise ignore event"
                stone_selected, curr_player, end = move_st(*trans_coord(*event.pos))
                draw_board(curr_player, end)
            else:                                                        #si no has clicado una pieza
                "User should click on a stone to select it"
                stone_selected = select_st(*trans_coord(*event.pos))

# Friendly finish-up:
pygame.quit()
