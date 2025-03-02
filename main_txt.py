"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Text handling of a simple tic-tac-toe-like board, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
"""

# Import initialization of the separately programmed abstract board:

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

if mode_game == "Counter":
	stones, select_st, move_st, draw_txt, counter = set_board_up()
else:
	stones, select_st, move_st, draw_txt = set_board_up()

from constants import BSIZ
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

# set_board_up() already selects a first stone
stone_selected = True

# Loop until game ends
curr_player=0
end = False
draw_txt(False)

while not end:
    while not stone_selected:
        i, j = input("Select stone coordinates: ").split() #te dice si realmente has cogido una piedra valida(puede que cojas una piedra del oponente o pones un punto fuera del tablero)
        stone_selected = select_st(int(i), int(j))
        draw_txt(end)
    while stone_selected and not end:
         if mode_game == "Default" and len(stones()) == BSIZ**2:
            end = True
         else:
            i, j = input("Select destination coordinates: ").split() #te dice si el lugar al que quieres mover la pieza es correcta. 
            stone_selected, curr_player, end = move_st(int(i), int(j))
            draw_txt(end)

# Wait for the user to look at the screen before ending the program.
input('\nGame Over')






