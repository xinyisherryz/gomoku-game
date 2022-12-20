import sys
sys.path.append("..")
from game_board import GameBoard  # nopep8


def test_constructor():
    """
    test the game board constructor
    """
    test_boardsize = 3
    test_board = GameBoard(test_boardsize)
    assert test_board.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
