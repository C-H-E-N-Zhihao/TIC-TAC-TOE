# Tic-Tac-Toe Variants

## Introduction
This project is a Python implementation of Tic-Tac-Toe and its various gameplay variants. It was developed as part of a group project, starting from an incomplete program provided by instructors. The goal was to create a functional Tic-Tac-Toe game playable in both terminal and graphical interfaces using the `pygame` module. This is a two-player game, and there is no AI opponent available.

## Features
- **Standard Tic-Tac-Toe**: Classic three-in-a-row win condition.
- **Counter Mode**: The winner is determined by the number of three-in-a-row alignments.
- **Moveable Mode**: After placing all pieces, players can move their stones.
  - **Middle Variant**: The game starts with the first move in the center.
  - **Adjacent Variant**: Pieces can only be moved to adjacent empty spaces.
- **Misery Mode**: The player who aligns three stones first loses.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd tic-tac-toe-variants
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```

## Usage
Run the game in either terminal or GUI mode:
```sh
python main_txt.py  # Terminal version
python main_gui.py  # Pygame version
```

At the start, players can select which variant to play and the board size using interactive input prompts.

- **In `main_txt.py`**: Players place pieces by typing `x y`, where `x` and `y` are within the range `[0, board_size]`. `x` represents the position on the x-axis, and `y` represents the position on the y-axis.
- **In `main_gui.py`**: Players place pieces by clicking directly on the corresponding position on the board.

## Code Structure
- **`main_txt.py`**: Terminal-based version of the game.
- **`main_gui.py`**: Graphical version using Pygame.
- **`constants.py`**: Contains game constants and settings.
- **Variant scripts**:
  - `default.py`: Standard Tic-Tac-Toe
  - `counter.py`: Counts alignments to determine the winner
  - `moveable.py`: Allows stone movement
  - `misery.py`: Reverse win condition

## Development Process
- Initial research involved studying Tic-Tac-Toe implementations online.
- A basic terminal version was created first.
- The graphical version was implemented using `pygame`.
- Variants were added incrementally, refining game logic.
- Debugging was done using print statements to track errors and logic flaws.

## Future Improvements
- Improve GUI with animations and better graphics.
- Implement AI for single-player mode.
- Add an online multiplayer mode.

## References
- [Tic-Tac-Toe implementation tutorial](https://youtu.be/Al917szWQXA)

## Authors
- Zhihao Chen & Pengcheng Chen
