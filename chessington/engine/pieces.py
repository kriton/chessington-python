from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_piece = board.find_piece(self)
        avail_moves:List[Square] = []
        if (self.player == Player.BLACK and current_piece.row - 2 > -1 ):

            if(board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col - 1)) and current_piece.col - 1 > -1 and
               board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col - 1)).player == Player.WHITE ):
                avail_moves.append(Square.at(current_piece.row - 1  ,current_piece.col - 1))
            
            if (board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col + 1)) and current_piece.col + 1 < 7 and
               board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col + 1)).player == Player.WHITE ):
                avail_moves.append(Square.at(current_piece.row - 1  ,current_piece.col + 1))

            if(not board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col))):
                avail_moves.append(Square.at(current_piece.row - 1  ,current_piece.col))
            
            if (current_piece.row == 6 and
                not board.get_piece(Square.at(current_piece.row - 2  ,current_piece.col)) and
                not board.get_piece(Square.at(current_piece.row - 1  ,current_piece.col))):
                avail_moves.append(Square.at(current_piece.row - 2 ,current_piece.col))

        elif(self.player == Player.WHITE and current_piece.row + 2 < 7 ):
            if(board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col - 1)) and current_piece.col - 1 > -1 and
               board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col - 1)).player == Player.BLACK ):
                avail_moves.append(Square.at(current_piece.row + 1  ,current_piece.col - 1))
            
            if (board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col + 1)) and current_piece.col + 1 < 7 and
                board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col + 1)).player == Player.BLACK ):
                avail_moves.append(Square.at(current_piece.row + 1  ,current_piece.col + 1))
            
            if(not board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col))):
                avail_moves.append(Square.at(current_piece.row + 1,current_piece.col))

            if (current_piece.row == 1 and current_piece.row + 2 < 8 and
                not board.get_piece(Square.at(current_piece.row + 2  ,current_piece.col)) and
                not board.get_piece(Square.at(current_piece.row + 1  ,current_piece.col))):
                avail_moves.append(Square.at(current_piece.row + 2 ,current_piece.col))

        return avail_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_piece = board.find_piece(self)
        avail_moves:List[Square]
        

        return []