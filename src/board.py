from settings import *
from utils.fen_parser import FenParser
from piece import *
from square import Square

class Board:

    def __init__(self) -> None:
        self.squares: list[list[Square]] = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create_board()
        self._add_pieces(STARTING_POSITION)

    def _create_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    def _add_pieces(self, fen):
        fen_parser = FenParser(fen)
        squares = fen_parser.parse()
        for row_index, row in enumerate(squares):
            for col_index, square in enumerate(row):
                if square == ' ':
                    pass
                else:
                    self._add_piece_to_square(row_index, col_index, get_piece_by_fen(square))

    def _add_piece_to_square(self, row, col, piece: Piece):
        self.squares[row][col] = Square(row, col, piece)
    
    def get_square(self, row, col):
        return self.squares[row][col]
    
    def get_piece(self, row, col):
        if self.has_piece(row, col):
            return self.get_square(row, col).piece
    
    def has_piece(self, row, col):
        return self.get_square(row, col).has_piece()