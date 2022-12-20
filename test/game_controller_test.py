import sys
sys.path.append("..")
from game_controller import GameController  # nopep8
from game_board import GameBoard  # nopep8
from stone import Stone  # nopep8


def test_constructor():
    """
    test the gc constructor
    """
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    # board.board
    assert test_gc.board.board == \
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert test_gc.cur_step == 0
    assert test_gc.allowMousePress is True


def test_create_stone():
    """
    test the method to create both human and ai stone
    """
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    test_x = 1
    test_y = 1
    test_size = 50
    test_player = "Human"
    test_gc.create_stone(test_x, test_y, test_size, test_player)
    test_gc.the_stone = Stone(test_x, test_y, test_size, test_player)
    assert test_gc.board.board == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert test_gc.cur_step == 1
    # better test the attributes to check
    assert test_gc.the_stone._x == 1
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    test_x = 2
    test_y = 1
    test_size = 50
    test_player = "AI"
    test_gc.create_stone(test_x, test_y, test_size, test_player)
    test_gc.the_stone = Stone(test_x, test_y, test_size, test_player)
    assert test_gc.board.board == [[0, 0, 0], [0, 0, 0], [0, 2, 0]]
    assert test_gc.cur_step == 1
    assert test_gc.the_stone._x == 2


def test_game_result():
    """
    test the method to asses game result/status
    """
    # test 5 in a row
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.board.board = [
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert test_gc.game_reuslt() == 1
    # test 5 in a col
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.board.board = [
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert test_gc.game_reuslt() == 2
    # test 5 from top left to down right
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.board.board = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert test_gc.game_reuslt() == 1
    # test 5 from top right to down left
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.board.board = [
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 0, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert test_gc.game_reuslt() == 2
    # test a draw
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.board.board = [
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert test_gc.game_reuslt() == -1


def test_get_distance():
    """
    test the method to calculate the distance between two spots
    """
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_x1 = 0
    test_y1 = 3
    test_x2 = 4
    test_y2 = 0
    assert test_gc.get_distance(test_x1, test_y1,
           test_x2, test_y2) == 5


def test_color_choice():
    """
    test the method to decide the color of the stone
    """
    test_boardsize = 6
    test_gc = GameController(test_boardsize)
    test_gc.cur_step = 4
    # need to add the () after color_choose
    assert test_gc.color_choose() == "Human"
    test_gc = GameController(test_boardsize)
    test_gc.cur_step = 3
    assert test_gc.color_choose() == "AI"
