import os

class Piece:
    def __init__(self, name, color, value, texture = None, texture_rect = None) -> None:
        self.name: str = name
        self.color = color
        value_sign = 1 if color == 'w' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def fen(self):
        return self.name.upper() if self.color == 'w' else self.name.lower()
    
    def set_texture(self, size = 90):
        self.size = size
        self.texture = os.path.join(
            f'assets/images/{size}px/{self.color}{self.name}.png')
    
    def add_moves(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color) -> None:
        self.dir = -1 if color == 'w' else 1
        super().__init__('P', color, 1.0)

class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__('N', color, 3.0)

class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__('B', color, 3.001)

class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__('R', color, 5.0)

class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__('Q', color, 9.0)

class King(Piece):
    def __init__(self, color) -> None:
        super().__init__('K', color, 10_000.0)

# Pieces Dictionary
def get_piece_by_fen(fen: str):
    if fen == 'P':
        return Pawn('w')
    if fen == 'p':
        return Pawn('b')
    if fen == 'N':
        return Knight('w')
    if fen == 'n':
        return Knight('b')
    if fen == 'B':
        return Bishop('w')
    if fen == 'b':
        return Bishop('b')
    if fen == 'R':
        return Rook('w')
    if fen == 'r':
        return Rook('b')
    if fen == 'Q':
        return Queen('w')
    if fen == 'q':
        return Queen('b')
    if fen == 'K':
        return King('w')
    if fen == 'k':
        return King('b')