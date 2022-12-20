import sys
sys.path.append("..")
from ai import AI  # nopep8
from game_controller import GameController  # nopep8


def test_constructor():
    """
    test the AI constructor
    """
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    test_ai = AI(test_gc)
    assert test_ai.chess_score == {
            "5": 10000,
            "4": 2500,
            "3": 500,
            "2": 100,
            "1": 0,
            }
    assert test_ai.ai_count == {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    assert test_ai.gc == test_gc


def test_choose_spot():
    """
    test the choose spot method
    """
    test_ai_coord_score = dict()
    test_x = 1
    test_y = 2
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    test_ai = AI(test_gc)
    test_ai.ai_count = {"5": 1, "4": 4, "3": 2, "2": 5, "1": 3}
    test_ai_score = test_ai.ai_count["5"] * test_ai.chess_score["5"] \
        + test_ai.ai_count["4"] * test_ai.chess_score["4"] \
        + test_ai.ai_count["3"] * test_ai.chess_score["3"] \
        + test_ai.ai_count["2"] * test_ai.chess_score["2"] \
        + test_ai.ai_count["1"] * test_ai.chess_score["1"]
    test_neighbor_score = 100
    test_ai_coord_score[test_x, test_y] = test_ai_score + test_neighbor_score
    assert test_ai_score == 21500
    assert test_ai_coord_score[test_x, test_y] == 21600
    test_x = 2
    test_y = 3
    test_ai.ai_count = {"5": 2, "4": 4, "3": 2, "2": 0, "1": 3}
    test_ai_score = test_ai.ai_count["5"] * test_ai.chess_score["5"] \
        + test_ai.ai_count["4"] * test_ai.chess_score["4"] \
        + test_ai.ai_count["3"] * test_ai.chess_score["3"] \
        + test_ai.ai_count["2"] * test_ai.chess_score["2"] \
        + test_ai.ai_count["1"] * test_ai.chess_score["1"]
    test_neighbor_score = 10
    test_ai_coord_score[test_x, test_y] = test_ai_score + test_neighbor_score
    assert test_ai_score == 31000
    assert test_ai_coord_score[test_x, test_y] == 31010
    test_max_score_coord = sorted(
        test_ai_coord_score.items(),
        key=lambda x: x[1],
        reverse=True
    )[0][0]
    assert test_max_score_coord == (2, 3)


def test_check_col():
    """
    test the method to check vertically
    """
    test_ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    size = 15
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for x in range(size - 5):
        for y in range(size):
            check_human = 0
            check_ai = 0
            for i in range(0, 5):
                if board[x + i][y] == 1:
                    check_human += 1
                if board[x + i][y] == 2:
                    check_ai += 1
            if check_ai == 5 and check_human == 0:
                test_ai_count["5"] += 1
            elif check_ai == 4 and check_human == 0:
                test_ai_count["4"] += 1
            elif check_ai == 3 and check_human == 0:
                test_ai_count["3"] += 1
            elif check_ai == 2 and check_human == 0:
                test_ai_count["2"] += 1
            elif check_ai == 1 and check_human == 0:
                test_ai_count["1"] += 1
    assert test_ai_count == {"5": 1, "4": 1, "3": 1, "2": 1, "1": 1}


def test_check_row():
    """
    test the method to check horizontally
    """
    test_ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    size = 15
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for y in range(size - 5):
        for x in range(size):
            check_human = 0
            check_ai = 0
            for i in range(0, 5):
                if board[x][y + i] == 1:
                    check_human += 1
                if board[x][y + i] == 2:
                    check_ai += 1
            if check_ai == 5 and check_human == 0:
                test_ai_count["5"] += 1
            elif check_ai == 4 and check_human == 0:
                test_ai_count["4"] += 1
            elif check_ai == 3 and check_human == 0:
                test_ai_count["3"] += 1
            elif check_ai == 2 and check_human == 0:
                test_ai_count["2"] += 1
            elif check_ai == 1 and check_human == 0:
                test_ai_count["1"] += 1
    assert test_ai_count == {"5": 1, "4": 2, "3": 2, "2": 2, "1": 5}


def test_check_diag_1():
    """
    test the method to check from bottom left to top right
    """
    test_ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    size = 15
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for x in range(size - 5 + 1):
        for y in range(size - 5 + 1):
            check_human = 0
            check_ai = 0
            for i in range(0, 5):
                if board[x + i][y + 5 - 1 - i] == 1:
                    check_human += 1
                if board[x + i][y + 5 - 1 - i] == 2:
                    check_ai += 1
            if check_ai == 5 and check_human == 0:
                test_ai_count["5"] += 1
            elif check_ai == 4 and check_human == 0:
                test_ai_count["4"] += 1
            elif check_ai == 3 and check_human == 0:
                test_ai_count["3"] += 1
            elif check_ai == 2 and check_human == 0:
                test_ai_count["2"] += 1
            elif check_ai == 1 and check_human == 0:
                test_ai_count["1"] += 1
    assert test_ai_count == {"5": 1, "4": 2, "3": 2, "2": 2, "1": 2}


def test_check_diag_2():
    """
    test the method to check from top left to bottom right
    """
    test_ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    size = 15
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for x in range(size - 5 + 1):
        for y in range(size - 5 + 1):
            check_human = 0
            check_ai = 0
            for i in range(0, 5):
                if board[x + 5 - 1 - i][y + 5 - 1 - i] == 1:
                    check_human += 1
                if board[x + 5 - 1 - i][y + 5 - 1 - i] == 2:
                    check_ai += 1
            if check_ai == 5 and check_human == 0:
                test_ai_count["5"] += 1
            elif check_ai == 4 and check_human == 0:
                test_ai_count["4"] += 1
            elif check_ai == 3 and check_human == 0:
                test_ai_count["3"] += 1
            elif check_ai == 2 and check_human == 0:
                test_ai_count["2"] += 1
            elif check_ai == 1 and check_human == 0:
                test_ai_count["1"] += 1
    assert test_ai_count == {"5": 1, "4": 2, "3": 2, "2": 2, "1": 2}


def test_neighbor_score():
    """
    test the method to score neighbor spot around a coord
    """
    size = 15
    test_x = 4
    test_y = 9
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board[test_x][test_y] = 2
    test_score = 0
    if test_x - 1 > 0:
        if board[test_x - 1][test_y] == 2:
            test_score += 20
        if board[test_x - 1][test_y] == 1:
            test_score += 10
    if test_x + 1 < size:
        if board[test_x + 1][test_y] == 2:
            test_score += 20
        if board[test_x + 1][test_y] == 1:
            test_score += 10
    if test_y - 1 > 0:
        if board[test_x][test_y - 1] == 2:
            test_score += 20
        if board[test_x][test_y - 1] == 1:
            test_score += 10
    if test_y + 1 < size:
        if board[test_x][test_y + 1] == 2:
            test_score += 20
        if board[test_x][test_y + 1] == 1:
            test_score += 10
    if test_x - 1 > 0 and test_y - 1 > 0:
        if board[test_x - 1][test_y - 1] == 2:
            test_score += 20
        if board[test_x - 1][test_y - 1] == 1:
            test_score += 10
    if test_x - 1 > 0 and test_y + 1 < size:
        if board[test_x - 1][test_y + 1] == 2:
            test_score += 20
        if board[test_x - 1][test_y + 1] == 1:
            test_score += 10
    if test_x + 1 < size and test_y - 1 > 0:
        if board[test_x + 1][test_y - 1] == 2:
            test_score += 20
        if board[test_x + 1][test_y - 1] == 1:
            test_score += 10
    if test_x + 1 < size and test_y + 1 < size:
        if board[test_x + 1][test_y + 1] == 2:
            test_score += 20
        if board[test_x + 1][test_y + 1] == 1:
            test_score += 10
    assert test_score == 100


def test_clear_count():
    """
    test the method to clear the count of ai streaks
    """
    test_boardsize = 3
    test_gc = GameController(test_boardsize)
    test_ai = AI(test_gc)
    test_ai.ai_count["5"] = 1
    test_ai.ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
    assert test_ai.ai_count["5"] == 0
