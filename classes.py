class Piece:
    """This is a MOTHER class for all the pieces"""
    
    move_history = []
    
    def show_legal_moves(self):
        pass
    
    def move(self):
        pass
    
    def legal_move_or_not(self):
        pass
    
    def capture(self):
        pass
    
    def king_check(self):
        pass
    
    


class Pawn(Piece):
    """This is the son class for the pawn"""
    
    def en_passant(self):
        pass
    
    def promotion(self):
        pass

class Rook(Piece):
    """This is the son class for the rook"""

class Knight(Piece):
    """This is the son class for the knight"""

class Bishop(Piece):
    """This is the son class for the bishop"""

class Queen(Piece):
    """This is the son class for the queen"""

class King(Piece):
    """This is the son class for the king"""
    def castle(self):
        pass