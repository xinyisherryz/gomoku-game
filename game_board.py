

class GameBoard:
    """
    A class representing the board
    """
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.board = [[0 for _x in range(self.boardsize)]
                      for _y in range(self.boardsize)]
