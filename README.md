# chess_variant_game: A Chess Variant Game

## Project Description
The purpose of this project is to work on the interaction between classes and objects and to reinforce foundational computer science skills. The project involves creating a class named ChessVar for playing an abstract board game that is a variant of chess. The project is implemented in Python.

### Game Overview
ChessVar is a chess variant with modified rules where the winner is the first player to capture all of an opponent's pieces of one type. The game starts with the standard chess setup, and the pieces move and capture as in traditional chess. However, there is no castling, en passant, or pawn promotion. The king is not a special piece in this game; there is no check or checkmate. Players take turns, with white moving first, and the game ends when one player captures all pieces of a specific type (e.g., all knights, pawns, or queens).

### Board Representation
Locations on the board are specified using "algebraic notation," with columns labeled a-h and rows labeled 1-8.

The game board is represented as an 8x8 list of lists, allowing access to a specific square with game_board[row][column].

### Classes and Methods
The ChessVar class includes the following:
- Initialization (__init__): Initializes data members, including the game board, player turns, and piece positions.
- Game State (get_game_state): Returns the current state of the game: 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'.
- Make Move (make_move): Takes two parameters (the square moved from and the square moved to) and handles the logic for making a move, capturing pieces, updating the game state, and switching turns.

Additional classes include:
- Pieces: Parent class for all chess pieces (Pawn, Rook, Knight, Bishop, King, and Queen), with methods to handle legal moves.
- Player: Parent class for White and Black players, tracking captured pieces.
- GameBoard: Initializes the board to the traditional chess setup and tracks piece positions throughout the game.

### Example Usage
Here's a simple example of how the `ChessVar` class could be used in Python:

```python
game = ChessVar()
move_result = game.make_move('a2', 'a4')
game.make_move('g1', 'f1')
state = game.get_game_state()
```

### Installation and Usage
- Clone the Repository: https://github.com/BraleeGilday/chess_variant_game.git
- Navigate to the Project Directory: cd ChessVar
- Run the Game: You can instantiate the ChessVar class and start making moves as shown in the example usage.
  
### Project Status
This project is currently complete, with potential for future enhancements, such as adding a graphical user interface or extending the rule set. Additionally, this program has not yet been evaluated for time or space complexity; better efficiency is likely possible. Future work can be done in improving this efficiency. 

### License
This project is licensed under the MIT License. See the LICENSE file for more information.

### Contact
Bralee Gilday - www.linkedin.com/in/bralee-gilday
