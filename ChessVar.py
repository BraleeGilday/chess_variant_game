# Author: Bralee Gilday
# GitHub username: BraleeGilday
# Date: 12/10/23
# Description: This is a program to play an abstract board game that is a variant of chess. The game follows modified
# rules where the winner is the first player to capture all of an opponent's pieces of one type. Pieces move and capture
# as in standard chess, excluding castling, en passant, and pawn promotion. The locations on the board are specified
# using "algebraic notation", with columns labeled a-h and rows labeled 1-8. The program includes a class named ChessVar
# for playing the game. This class includes an initialization method, a method to get the game state ('UNFINISHED',
# 'WHITE_WON', or 'BLACK_WON'), and a method to make moves. Players take turns, and the game ends when one player
# captures all pieces of a specific type. Additionally, the program defines classes for chess pieces (Pawn, Rook,
# Knight, Bishop, King, and Queen), which are all children of the parent class Pieces. Each piece class has a move
# method to handle legal moves. The program also defines classes for players (White and Black), which are children of
# the parent class Player. The Player classes keep track of captured pieces. Finally, the program defines a GameBoard
# class, which initializes the game board to be set up as in traditional chess, then keeps track of where the pieces are
# on the board as the game continues.

class Pieces:
    """
    Represents a piece on a chess board.

    This is the parent class to Pawn, Rook, Knight, Bishop, King, and Queen classes. These classes will communicate with
    the GameBoard class in order to initialize the chess board with the necessary white and black pieces and to check
    whether certain squares on the game board are occupied. This class communicates with the ChessVar class to determine
    if a given move is valid.
    """

    def __init__(self, player):
        """
        Creates a piece in a chess game that either belongs to "WHITE" or "BLACK".

        Parameter:
        - player (str): Represents the color of the piece and therefore the player who the piece belongs to;
        either "WHITE" or "BLACK".
        """
        self._player_it_belongs_to = player    # in the future, this could also take a Player object, not just a string

    def get_player_it_belongs_to(self):
        """Returns the player the Piece belongs to"""
        player = self._player_it_belongs_to  # Either "WHITE" or "BLACK"
        return player
    

class Pawn(Pieces):
    """
    Represents a pawn piece in a game of chess.
    Inherits from Pieces.
    Will communicate with GameBoard to initialize the Pawn pieces at the start of a new game. Will also communicate with
    ChessVar in order to determine if a move by a Pawn piece is valid.
    """

    def __init__(self, player):
        """Creates a Pawn, which is a Piece, with a player associated (either "WHITE" or "BLACK"). The pawn is also
        initialized to be ready for its first move."""
        super().__init__(player)  # calls parent class, Pieces, __init__ method
        self._first_move = True

    def get_piece_type(self):
        """
        Returns "Pawn" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "Pawn"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a Pawn can make.

        If it is a pawn's first move, it can move forward one or two squares. If a pawn has already moved, then it can
        move forward just one square at a time. It captures by moving diagonally forward to the left or right (as long
        as there is an opponent's piece there to be captured). A pawn cannot move to a square if it is occupied by
        another piece, unless it is capturing an opponent's piece.

        Takes three parameters:
        -game_board: The current game board of the chess game in progress; this is a list of eight dictionaries.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal and valid.
        Returns False if the given move is illegal or not valid.
        """

        # allows us to perform operations on the column letters, by associating each letter with an index number.
        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])

        # Need to distinguish between WHITE and BLACK pieces since moving "forward" is different for each side.
        if self.get_player_it_belongs_to() == "WHITE":
            if self._first_move is True:    # If it is the pawn's first move:
                # If the pawn is trying to move forward one square
                possible = str(from_square[0] + str(int(from_square[1]) + 1))
                if possible == to_square and game_board.get_status_of_square(possible) is None:
                    self._first_move = False
                    return True
                # If the pawn is trying to move forward two squares
                if game_board.get_status_of_square(possible) is None:
                    possible = str(from_square[0] + str(int(from_square[1]) + 2))
                    if possible == to_square and game_board.get_status_of_square(possible) is None:
                        self._first_move = False
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the left.
                if current_column_as_int > 0:   # ensures current_column_as_int will work correctly without error
                    possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) + 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        self._first_move = False
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the right.
                if current_column_as_int < 7:
                    possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) + 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        self._first_move = False
                        return True

                return False    # Not a valid move for this pawn from from_square to to_square

            if self._first_move is False:  # if the pawn has already been moved
                # If the pawn is trying to move forward one square
                possible = str(from_square[0] + str(int(from_square[1]) + 1))
                if possible == to_square and game_board.get_status_of_square(possible) is None:
                    return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the left.
                if current_column_as_int > 0:
                    possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) + 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the right.
                if current_column_as_int < 7:
                    possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) + 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        return True

                return False    # Not a valid move for this pawn from from_square to to_square

        else:   # If pawn is "BLACK"
            if self._first_move is True:
                # If the pawn is trying to move forward one square
                possible = str(from_square[0] + str(int(from_square[1]) - 1))
                if possible == to_square and game_board.get_status_of_square(possible) is None:
                    self._first_move = False
                    return True

                # If the pawn is trying to move forward two squares
                if game_board.get_status_of_square(possible) is None:
                    possible = str(from_square[0] + str(int(from_square[1]) - 2))
                    if possible == to_square and game_board.get_status_of_square(possible) is None:
                        self._first_move = False
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the left.
                if current_column_as_int < 7:
                    possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) - 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        self._first_move = False
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the right.
                if current_column_as_int > 1:
                    possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) - 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        self._first_move = False
                        return True

                return False

            if self._first_move is False:  # if the BLACK pawn has already been moved
                # If the pawn is trying to move forward one square
                possible = str(from_square[0] + str(int(from_square[1]) - 1))
                if possible == to_square and game_board.get_status_of_square(possible) is None:
                    return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the left.
                if current_column_as_int < 7:
                    possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) - 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        return True

                # If the pawn is trying to capture an opponent's piece by moving diagonally to the right.
                if current_column_as_int > 1:
                    possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) - 1))
                    if possible == to_square and game_board.get_status_of_square(possible) is not None:
                        return True

                return False


class Rook(Pieces):
    """
    Represents a rook piece in a game of chess.
    Inherits from Pieces.
    Will communicate with GameBoard to initialize the Pawn pieces at the start of a new game. Will also communicate with
    ChessVar in order to determine if a move by a Rook piece is valid.
    """

    def __init__(self, player):
        """Creates a Rook, which is a Piece, with a player associated (either "WHITE" or "BLACK")"""
        super().__init__(player)  # calls parent class, Pieces, __init__ method

    def get_piece_type(self):
        """
        Returns "Rook" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "Rook"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a Rook can make.

        A rook can move as many squares as it likes left or right horizontally, or as many squares as it likes up or
        down vertically (as long as it isn't blocked by other pieces). A rook captures a player's piece by landing
        on the square that is occupied by an opponent's piece.

        Takes three parameters:
        -game_board: The current game board of the chess game in progress; this is a list of eight dictionaries.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal and valid.
        Returns False if the given move is illegal or not valid.
        """
        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])   # the column "index number" of the from_square
        to_column_as_int = column_list.index(to_square[0])          # the column "index number" of the to_square

        # White rook moving forward/Black rook moving backwards
        if to_square[1] > from_square[1] and to_square[0] == from_square[0]:
            difference_of_square_spaces = int(to_square[1])-int(from_square[1])
            # checking o make sure the squares along the way are unoccupied
            for num in range(difference_of_square_spaces - 1):
                on_route = str(from_square[0] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False    # the path to the to_square is not clear
            else:
                return True     # the path to the to_square is clear

        # White rook moving backward/Black rook moving forwards
        if to_square[1] < from_square[1] and to_square[0] == from_square[0]:
            difference_of_square_spaces = int(from_square[1]) - int(to_square[1])
            for num in range(difference_of_square_spaces - 1):
                on_route = str(from_square[0] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # White rook moving right/Black rook moving left
        if current_column_as_int < to_column_as_int:
            difference_of_square_spaces = to_column_as_int - current_column_as_int
            # Checks that the row number stays the same (ensuring the rook moves in a straight line)
            if to_square[1] == from_square[1]:
                for num in range(difference_of_square_spaces - 1):
                    on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1])))
                    if game_board.get_status_of_square(on_route) is not None:
                        return False
                else:
                    return True

        # White rook moving left/Black rook moving right
        if current_column_as_int > to_column_as_int:
            difference_of_square_spaces = current_column_as_int - to_column_as_int
            # Checks that the row number stays the same (ensuring the rook moves in a straight line)
            if to_square[1] == from_square[1]:
                for num in range(difference_of_square_spaces - 1):
                    on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1])))
                    if game_board.get_status_of_square(on_route) is not None:
                        return False
                else:
                    return True

        return False


class Knight(Pieces):
    """
    Represents a knight piece in a game of chess.

    A knight moves one square left or right horizontally and then two squares up or down vertically, or it moves two
    squares left or right horizontally and then one square up or down vertically. A knight captures a player's piece by
    landing on a square that is occupied by an opponent's piece.

    Inherits from Pieces.

    Will communicate with GameBoard to initialize the Knight pieces at the start of a new game. Will also communicate
    with ChessVar in order to determine if a move by a Knight is valid.
    """

    def __init__(self, player):
        """Creates a knight, which is a Piece, with a player associated (either "WHITE" or "BLACK")"""
        super().__init__(player)  # calls parent class, Pieces, __init__ method

    def get_piece_type(self):
        """
        Returns "Knight" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "Knight"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a Knight can make.

        Takes three parameters:
        -game_board: The current game board of the chess game in progress; this is a list of eight dictionaries.
            # game_board not actually used by this Knight method; in the future, could fix this.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal.
        Returns False if the given move is illegal.
        """

        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])

        # If the knight is trying to move 1 left and 2 up (from WHITE's perspective)
        if current_column_as_int > 0:
            possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) + 2))
            if possible == to_square:
                return True

        # If the knight is trying to move 1 left and 2 down (from WHITE's perspective)
        if current_column_as_int > 0:
            possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) - 2))
            if possible == to_square:
                return True

        # If the knight is trying to move 1 right and 2 up (from WHITE's perspective)
        if current_column_as_int < 7:
            possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) + 2))
            if possible == to_square:
                return True

        # If the knight is trying to move 1 right and 2 down (from WHITE's perspective)
        if current_column_as_int < 7:
            possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) - 2))
            if possible == to_square:
                return True

        # If the knight is trying to move 2 left and 1 up (from WHITE's perspective)
        if current_column_as_int > 1:
            possible = str(column_list[current_column_as_int - 2] + str(int(from_square[1]) + 1))
            if possible == to_square:
                return True

        # If the knight is trying to move 2 left and 1 down (from WHITE's perspective)
        if current_column_as_int > 1:
            possible = str(column_list[current_column_as_int - 2] + str(int(from_square[1]) - 1))
            if possible == to_square:
                return True

        # If the knight is trying to move 2 right and 1 up (from WHITE's perspective)
        if current_column_as_int < 6:
            possible = str(column_list[current_column_as_int + 2] + str(int(from_square[1]) + 1))
            if possible == to_square:
                return True

        # If the knight is trying to move 2 right and 1 down (from WHITE's perspective)
        if current_column_as_int < 6:
            possible = str(column_list[current_column_as_int + 2] + str(int(from_square[1]) - 1))
            if possible == to_square:
                return True

        return False


class Bishop(Pieces):
    """
    Represents a bishop piece in a game of chess.

    A bishop can move diagonally as many squares as it likes, as long as it is not blocked by its own pieces or an
    occupied square. It can capture an opponent's piece by moving to the occupied square where the piece is located.

    Inherits from Pieces.

    Will communicate with GameBoard to initialize the Bishop pieces at the start of a new game. Will also communicate
    with ChessVar in order to determine if a move by a Bishop is valid.
    """

    def __init__(self, player):
        """Creates a Bishop, which is a Piece, with a player associated (either "WHITE" or "BLACK")"""
        super().__init__(player)  # calls parent class, Pieces, __init__ method

    def get_piece_type(self):
        """
        Returns "Bishop" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "Bishop"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a Bishop can make.

        Takes three parameters:
        -game board: The current game board of the chess game in progress; this is a list of eight dictionaries.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal.
        Returns False if the given move is illegal.
        """

        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])   # the column "index number" of the from_square
        to_column_as_int = column_list.index(to_square[0])          # the column "index number" of the to_square

        difference_on_x_axis = to_column_as_int - current_column_as_int    # change in column "letter"
        difference_on_y_axis = int(to_square[1]) - int(from_square[1])     # change in column "number"

        # Moving diagonally forward to the right (from White's perspective)
        if difference_on_x_axis > 0 and difference_on_y_axis > 0 and difference_on_y_axis/difference_on_x_axis == 1:
            # Check if both changes are positive and the ratio of change is 1:1, which confirms a diagonal move
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally forward to the left (from White's perspective)
        if difference_on_x_axis < 0 < difference_on_y_axis and difference_on_y_axis/difference_on_x_axis == -1:
            # Check if change in x is negative and change in y is positive and the ratio of change is -1:1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally backwards to the right (from White's perspective)
        if difference_on_x_axis > 0 > difference_on_y_axis and difference_on_y_axis/difference_on_x_axis == -1:
            # Check if the ratio of change is 1:-1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally backwards to the left (from White's perspective)
        if difference_on_x_axis < 0 and difference_on_y_axis < 0 and difference_on_y_axis/difference_on_x_axis == 1:
            # Check if the ratio of change is -1:-1 which is equal to 1:1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        return False


class King(Pieces):
    """
    Represents a king piece in a game of chess.

    The king can only move (or capture) one square in any direction.

    Inherits from Pieces.

    Will communicate with GameBoard to initialize the King pieces at the start of a new game. Will also communicate
    with ChessVar in order to determine if a move by a King is valid.
    """

    def __init__(self, player):
        """Creates a king, which is a Piece, with a player associated (either "WHITE" or "BLACK")"""
        super().__init__(player)  # calls parent class, Pieces, __init__ method

    def get_piece_type(self):
        """
        Returns "King" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "King"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a King can make.

        Takes three parameters:
        -game_board: The current game board of the chess game in progress; this is a list of eight dictionaries.
            # game_board not actually used by this King method; in the future, could fix this.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal.
        Returns False if the given move is illegal.
        """

        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])

        # If the king is trying to move up 1 square (from white's perspective)
        possible = str(from_square[0] + str(int(from_square[1]) + 1))
        if possible == to_square:
            return True

        # If the king is trying to move down 1 square (from white's perspective)
        possible = str(from_square[0] + str(int(from_square[1]) - 1))
        if possible == to_square:
            return True

        # If the king is trying to move 1 square to the left (from White's perspective)
        if current_column_as_int > 1:
            possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1])))
            if possible == to_square:
                return True

        # If the king is trying to move 1 square to the right (from White's perspective)
        if current_column_as_int < 7:
            possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1])))
            if possible == to_square:
                return True

        # If the king is trying to move forward diagonally to the left (from White's perspective)
        if current_column_as_int > 1:
            possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) + 1))
            if possible == to_square:
                return True

        # If the king is trying to move forward diagonally to the right (from White's perspective)
        if current_column_as_int < 7:
            possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) + 1))
            if possible == to_square:
                return True

        # If the king is trying to move backward diagonally to the left (from White's perspective)
        if current_column_as_int > 1:
            possible = str(column_list[current_column_as_int - 1] + str(int(from_square[1]) - 1))
            if possible == to_square:
                return True

        # If the king is trying to move backward diagonally to the right (from White's perspective)
        if current_column_as_int < 7:
            possible = str(column_list[current_column_as_int + 1] + str(int(from_square[1]) - 1))
            if possible == to_square:
                return True

        return False


class Queen(Pieces):
    """
    Represents a queen piece in a game of chess.

    The queen can move as many squares as it likes left or right horizontally, or as many squares as it likes up or down
    vertically, or as many squares as it likes diagonally (as long as it is not blocked by its own pieces or an
    occupied square). It can capture an opponent's piece by moving to the occupied square where the piece is located.

    Inherits from Pieces.

    Will communicate with ChessVar to initialize the Queen pieces at the start of a new game. Will also communicate
    with ChessVar in order to determine if a move by a Queen is valid.
    """

    def __init__(self, player):
        """Creates a Queen, which is a Piece, with a player associated (either "WHITE" or "BLACK")"""
        super().__init__(player)  # calls parent class, Pieces, __init__ method

    def get_piece_type(self):
        """
        Returns "Queen" (the type of chess piece an object of this class is).
        This method is used by the Player class once there is a capture to determine what type of piece has been
        captured.
        """
        return "Queen"

    def move(self, from_square, to_square, game_board):
        """
        Represents the legal moves that a Queen can make.

        Takes two parameters:
        -game_board: The current game board of the chess game in progress; this is a list of eight dictionaries.
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to

        Returns True if the given move is legal.
        Returns False if the given move is illegal.
        """

        column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_column_as_int = column_list.index(from_square[0])   # the column "index number" of the from_square
        to_column_as_int = column_list.index(to_square[0])          # the column "index number" of the to_square

        difference_on_x_axis = to_column_as_int - current_column_as_int    # change in column "letter"
        difference_on_y_axis = int(to_square[1]) - int(from_square[1])     # change in column number

        # Moving diagonally forward to the right (from White's perspective)
        if difference_on_x_axis > 0 and difference_on_y_axis > 0 and difference_on_y_axis/difference_on_x_axis == 1:
            # Check if both changes are positive and the ratio of change is 1:1, which confirms a diagonal move
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally forward to the left (from White's perspective)
        if difference_on_x_axis < 0 < difference_on_y_axis and difference_on_y_axis/difference_on_x_axis == -1:
            # Check if change in x is negative and change in y is positive and the ratio of change is -1:1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally backwards to the right (from White's perspective)
        if difference_on_x_axis > 0 > difference_on_y_axis and difference_on_y_axis/difference_on_x_axis == -1:
            # Check if the ratio of change is 1:-1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving diagonally backwards to the left (from White's perspective)
        if difference_on_x_axis < 0 and difference_on_y_axis < 0 and difference_on_y_axis/difference_on_x_axis == 1:
            # Check if the ratio of change is -1:-1 which is equal to 1:1
            for num in range(abs(difference_on_x_axis) - 1):
                on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving forward in straight line (from White's perspective)
        if to_square[1] > from_square[1] and to_square[0] == from_square[0]:
            difference_of_square_spaces = int(to_square[1])-int(from_square[1])
            for num in range(difference_of_square_spaces - 1):
                on_route = str(from_square[0] + str(int(from_square[1]) + (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving backward in straight line (White's perspective)
        if to_square[1] < from_square[1] and to_square[0] == from_square[0]:
            difference_of_square_spaces = int(from_square[1]) - int(to_square[1])
            for num in range(difference_of_square_spaces - 1):
                on_route = str(from_square[0] + str(int(from_square[1]) - (num + 1)))
                if game_board.get_status_of_square(on_route) is not None:
                    return False
            else:
                return True

        # Moving right in a straight line (from White's perspective)
        if current_column_as_int < to_column_as_int:
            difference_of_square_spaces = to_column_as_int - current_column_as_int
            if to_square[1] == from_square[1]:
                for num in range(difference_of_square_spaces - 1):
                    on_route = str(column_list[current_column_as_int + (num + 1)] + str(int(from_square[1])))
                    if game_board.get_status_of_square(on_route) is not None:
                        return False
                else:
                    return True

        # Moving left in a straight line (from White's perspective)
        if current_column_as_int > to_column_as_int:
            difference_of_square_spaces = current_column_as_int - to_column_as_int
            if to_square[1] == from_square[1]:
                for num in range(difference_of_square_spaces - 1):
                    on_route = str(column_list[current_column_as_int - (num + 1)] + str(int(from_square[1])))
                    if game_board.get_status_of_square(on_route) is not None:
                        return False
                else:
                    return True

        return False


class Player:
    """
    Represents a player in the game of chess. A player can be either "WHITE" or "BLACK". A player will keep
    track of the pieces that a Player has left to capture from their opponent.

    This class is the parent class to the White and Black classes. These classes will communicate with ChessVar in order
    to find out when a piece has been captured. These classes will then communicate with inherited Pieces classes to
    get the piece type. It will also communicate with ChessVar to update the game state.
    """

    def __init__(self):
        """
        Creates a player in the game. This player is initialized to have captured none of its opponent's pieces.

        One private data member:
        -captured_pieces: A dictionary to keep track of captured pieces by a specific player. The keys of the
        dictionary are strings of the names of the possible chess pieces ("Pawn", "Rook", "Knight", "Bishop:, "King",
        "Queen") and the corresponding values are the number of a specific piece that the player's opponent still has
        left on the board. The values on the dictionary are initialized to the standard number of each type of piece.

        """
        self._pieces_left_to_capture = {
            "Pawn": 8,  # 8 total pawns per player
            "Rook": 2,  # 2 total rooks per player
            "Knight": 2,  # 2 total knights per player
            "Bishop": 2,  # 2 total bishops per player
            "King": 1,  # 1 king per player
            "Queen": 1  # 1 queen per player
        }

        # In the future, I would like to initialize all the values to 0 and keep track of pieces captured (rather than
        # pieces left).

    def get_pieces_left_to_capture(self):
        """Returns the dictionary with the number of pieces of each type that are left on the board for an opponent."""
        return self._pieces_left_to_capture

    def update_pieces_left_to_capture(self, captured_piece):
        """
        Updates how many pieces of each type a Player's opponent has left on the board (by updating the value for
        the key that matches the type of piece that was captured) in the pieces_left_to_capture dictionary.

        Communicates with Pieces classes to get the piece type of the Pieces object.
        """
        type_of_piece = captured_piece.get_piece_type()
        self._pieces_left_to_capture[type_of_piece] -= 1


class White(Player):
    """Represents the "WHITE" player in the chess game"""

    def __init__(self):
        """Creates a "WHITE" player in the game"""
        super().__init__()  # calls parent class (Player) __init__ method (not necessary)

    def check_for_win(self):
        """
        Checks if the Player has captured all of a specific type of piece (by checking if there are 0 left of any one
        piece). If the Player has captures all of one type of piece, then that Player has won the game.

        Communicates with the ChessVar class (specifically the make_move method) after a capture to check the status
        of the game.

        Returns "UNFINISHED" if the player has not won the game and the game should continue.
        Returns "WHITE_WON" if the player has won the game and the game should end.
        """
        for item in self._pieces_left_to_capture:
            if self._pieces_left_to_capture[item] == 0:
                return "WHITE_WON"
        else:
            return "UNFINISHED"


class Black(Player):
    """Represents the "BLACK" player in the chess game"""

    def __init__(self):
        """Creates a "BLACK" player in the game"""
        super().__init__()  # calls parent class (Player) __init__ method

    def check_for_win(self):
        """
        Checks if the Player has captured all of a specific type of piece (by checking if there are 0 left of any one
        piece). If the Player has captures all of one type of piece, then that Player has won the game.

        Communicates with the ChessVar class (specifically the make_move method) after a capture to check the status
        of the game.

        Returns "UNFINISHED" if the player has not won the game and the game should continue.
        Returns "BLACK_WON" if the player has won the game and the game should end.
        """
        for item in self._pieces_left_to_capture:
            if self._pieces_left_to_capture[item] == 0:
                return "BLACK_WON"
        else:
            return "UNFINISHED"


class GameBoard:
    """Represents the game board in a game of chess, which includes the set-up of the 32 different pieces."""
    def __init__(self):
        """
        Creates a game board with pieces for a game of chess. Takes no parameters.

        Locations on the board are specified using "algebraic notation," with columns labeled a-h and rows labeled 1-8.

        The game board is represented as list of eight dictionaries. Each dictionary represents a row on the game board.
        The keys of the dictionaries are strings of the algebraic location and the corresponding value is either the
        Piece object that is located at that square or None if no Piece is located at the square.

        Initialized to the normal starting position of standard chess. Communicates with the Pieces classes to
        initialize the Pieces objects on the board.

        """
        self._game_board = [
            {'a1': Rook("WHITE"), 'b1': Knight("WHITE"), 'c1': Bishop("WHITE"), 'd1': Queen("WHITE"),
             'e1': King("WHITE"), 'f1': Bishop("WHITE"), 'g1': Knight("WHITE"), 'h1': Rook("WHITE")},

            {'a2': Pawn("WHITE"), 'b2': Pawn("WHITE"), 'c2': Pawn("WHITE"), 'd2': Pawn("WHITE"), 'e2': Pawn("WHITE"),
             'f2': Pawn("WHITE"), 'g2': Pawn("WHITE"), 'h2': Pawn("WHITE")},

            {'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None},

            {'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None},

            {'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None},

            {'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None},

            {'a7': Pawn("BLACK"), 'b7': Pawn("BLACK"), 'c7': Pawn("BLACK"), 'd7': Pawn("BLACK"), 'e7': Pawn("BLACK"),
             'f7': Pawn("BLACK"), 'g7': Pawn("BLACK"), 'h7': Pawn("BLACK")},

            {'a8': Rook("BLACK"), 'b8': Knight("BLACK"), 'c8': Bishop("BLACK"), 'd8': Queen("BLACK"),
             'e8': King("BLACK"), 'f8': Bishop("BLACK"), 'g8': Knight("BLACK"), 'h8': Rook("BLACK")}
        ]

        self._boundaries = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
                            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
                            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
                            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
                            "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
                            "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
                            "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
                            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]

    def get_game_board(self):       # Currently not used, but can be used to "see" the game board.
        """
        Returns the game board, which is labeled using "algebraic notation" (columns labeled a-h
        and rows labeled 1-8).  The game board is represented by a list of eight dictionaries.
        Each dictionary represents a row on the game board. The keys of the dictionary are strings of the algebraic
        location and the corresponding value is either the Piece object that is located at that square or None if no
        Piece is located at the square.
        """
        return self._game_board

    def get_status_of_square(self, square):
        """
        Checks a given square on the game board to find out what piece (if any) is there.

        Returns either the Piece object that is located at that given square or None (if the square is not occupied)

        Parameter:
        -square: The column and row for a given square (algebraic notation)
        """
        for item in self._game_board:   # "item" is a dictionary in the list
            if square in item:          # if the given square is a key in the dictionary
                current_piece = item[square]
                return current_piece

    def update_game_board(self, square, piece):
        """
        Updates the game board by making sure pieces are moved and/or removed as directed by the make_move method in
        ChessVar.

        Either updates the given piece to be located at the given square, or it updates the given square to None
        (if piece is None).

        Takes two parameters:
        -square (str): The column and row for a given square (algebraic notation)
        -piece: Either a Pieces object or None
        """

        for item in self._game_board:
            if square in item:
                item[square] = piece

    def check_boundaries(self, square):
        """
        Checks whether a given square in within the boundaries of the game board.

        Returns True if the square is within the boundaries.
        Returns False if the square is not within the boundaries.

        Parameter:
        -square: The column and row for a given square (algebraic notation)
        """
        if square in self._boundaries:
            return True

        else:
            return False


class ChessVar:
    """
    Represents an abstract board game that is a variant of chess.

    The game follows modified rules where the winner is the first player to capture all of an opponent's pieces of one
    type. In this game, the king isn't a special piece, and there is no check or checkmate. Pieces move and capture as
    in standard chess, excluding castling, en passant, and pawn promotion.

    Locations on the board are specified using "algebraic notation," with columns labeled a-h and rows labeled 1-8.

    This class communicates with the Pieces classes, Players classes, and GameBoard class. It communicates with the
    GameBoard class to initialize a game board that is set up like a standard game of chess. It communicates with the
    Pieces classes to keep track of whether a move by a particular piece is valid. It will communicate with the Players
    classes to initialize two players in the game (one playing with "WHITE" pieces and one playing with "BLACK" pieces),
    and to keep track of how many of each type of chess piece has been captured by each of the players. This information
    will also inform the game state.
    """

    def __init__(self):
        """
        Initializes a game of a chess variant. Takes no parameters.

        The following private data members are initialized:

        -whose_turn_it_is (str): Keeps track of which player's turn it is. Will be either "WHITE" or "BLACK".
        Initialized to "WHITE", which means the White player will move first.

        -game_state (str): Keeps track of the state of the game. Will be either 'UNFINISHED', 'WHITE_WON', or
        'BLACK_WON'. Initialized to "UNFINISHED".

        -player1: A White object. This represents the player who will use white pieces for the chess game.

        -player2: A Black object. This represents the player who will use black pieces for the chess game.

        -game_board = A GameBoard object. This represents the game board for a chess game.

        """
        self._whose_turn_it_is = "WHITE"  # Can be either "WHITE" or "BLACK"
        self._game_state = "UNFINISHED"  # Can be either 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        self._player1 = White()  # Initializes the player who will move White pieces.
        self._player2 = Black()  # Initializes the player who will move Black pieces.
        self._game_board = GameBoard()  # Initializes the game board for the game of chess.

    def get_game_state(self):
        """Returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'"""
        return self._game_state

    def get_whose_turn_it_is(self):
        """Returns whose turn it is (either 'WHITE' or 'BLACK')"""
        return self._whose_turn_it_is

    def make_move(self, from_square, to_square):
        """
        Attempts to move a piece on the chess board, which is labeled using "algebraic notation" (columns labeled a-h
        and rows labeled 1-8).

        If the square being moved from does not contain a piece belonging to the player whose turn it is,
        or if the indicated move is not legal, or if the game has already been won, then it returns False.
        Otherwise, it makes the indicated move, removes any captured piece, updates the game state if necessary,
        updates whose turn it is, and returns True.

        This method will first check to make sure that the given from_square is occupied by a piece of the correct
        color. If so, the method will call on the move method from the given Piece object in order to determine whether
        a given move is legal. It will also call on the update_captured_pieces method from the inherited Player classes
        if a piece is captured.

        Takes two parameters:
        -from_square (str): represents the square the piece is moving from
        -to_square (str): represents the square that the piece is trying to move to
        """
        # Saves the Pieces object (or None) at the from_square and to_square
        current_piece = self._game_board.get_status_of_square(from_square)
        moving_to_status = self._game_board.get_status_of_square(to_square)

        if self._game_state != "UNFINISHED":
            # if the game has already been won
            return False

        if self._game_board.check_boundaries(from_square) is False:
            # if the square that is being moved from is not on the board
            return False

        if self._game_board.check_boundaries(to_square) is False:
            # if the square being moved to is not on the board
            return False

        if current_piece is None:
            # if there is no piece at the starting square
            return False

        if self._whose_turn_it_is != current_piece.get_player_it_belongs_to():
            # if the square being moved from does not contain a piece belonging to the player whose turn it is
            return False

        else:
            if moving_to_status is not None:    # if the to_square is occupied
                if self._whose_turn_it_is == moving_to_status.get_player_it_belongs_to():
                    # if the square being moved to is occupied by a piece of the same color
                    return False

            try_move = current_piece.move(from_square, to_square, self._game_board)     # checking if a move is valid

            if try_move is False:   # if the Pieces class determined the move was not valid
                return False

            if try_move is True:    # if the Pieces class determined the move was valid

                if moving_to_status is not None:    # if there is an opponent's piece at the to_square
                    captured_piece = moving_to_status
                    if self.get_whose_turn_it_is() == "WHITE":
                        self._player1.update_pieces_left_to_capture(captured_piece)     # update captured pieces
                        self._game_state = self._player1.check_for_win()                # update game state

                    if self.get_whose_turn_it_is() == "BLACK":
                        self._player2.update_pieces_left_to_capture(captured_piece)
                        self._game_state = self._player2.check_for_win()

                    # removes captured piece on the square by replacing it with the current piece
                    self._game_board.update_game_board(to_square, current_piece)

                else:   # if the square being moved to is empty
                    self._game_board.update_game_board(to_square, current_piece)    # moves the piece to the to_square

        # remove the piece from the starting square
        self._game_board.update_game_board(from_square, None)

        # Switch turns
        if self._whose_turn_it_is == "WHITE":
            self._whose_turn_it_is = "BLACK"
            return True

        if self._whose_turn_it_is == "BLACK":
            self._whose_turn_it_is = "WHITE"
            return True
