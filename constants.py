
while True:	
	BSIZ = int(input("\nWhat board size do you want? Type a number(3,5,7 or 9): ")) # board side size
	if BSIZ != 3 and BSIZ != 5 and BSIZ != 7 and BSIZ != 9:
		print("\nYou can only write 3, 5, 7 or 9.")
	else:
		break

ST_PLAYER = 4 # stones per player

# Define the colors we will use in RGB format
BLACK =   (  0,   0,   0)
GRAY =    (150, 150, 150) 
WHITE =   (255, 255, 255)
# Chosen so that they are still friendly to colorblind people:
BLUISH =  ( 26, 133, 255)
REDDISH = (212,  17,  89)
PURPLE = (128, 0, 128)
PLAYER_COLOR = (BLUISH, REDDISH) 

# Define the game window width and height and the slot size and separation in pixels
SLOT = 450//BSIZ        # squares size
SEP = 90//BSIZ          # squares separation
ROOM = SLOT + SEP # extra room at sides 
HEIGHT = BSIZ * SLOT + (BSIZ + 1) * SEP + ROOM # room for 3 squares with margin and internal separators and extra below
WIDTH = HEIGHT + ROOM              # extra at both sides
RAD = SLOT / 3                     # circle radius

NO_PLAYER = -1

