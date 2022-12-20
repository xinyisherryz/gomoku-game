import copy

HUMAN_STONE = 1
AI_STONE = 2
FIVE = 5
FOUR = 4
THREE = 3
TWO = 2
ONE = 1
FACTOR = 0.5


class AI:
    """
    AI player class
    """
    def __init__(self, gc):
        self.gc = gc
        self.chess_score = {
            "5": 10000,
            "4": 2500,
            "3": 500,
            "2": 100,
            "1": 0,
        }
        self.ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}

    # Public
    def choose_spot(self):
        """
        score each possible spot
        and return the spot with
        highest score
        None -> Int, Int
        """
        ai_coord_score = dict()
        size = self.gc.board.boardsize
        for x in range(size):
            for y in range(size):
                # only test if the spot has no stone
                if self.gc.board.board[x][y] == 0:
                    self._check_row(x, y)
                    self._check_col(x, y)
                    self._check_diag_1(x, y)
                    self._check_diag_2(x, y)
                    ai_score = self.ai_count["5"] * self.chess_score["5"] \
                        + self.ai_count["4"] * self.chess_score["4"] \
                        + self.ai_count["3"] * self.chess_score["3"] \
                        + self.ai_count["2"] * self.chess_score["2"] \
                        + self.ai_count["1"] * self.chess_score["1"]
                    neighbor_score = self._neighbor_score(x, y)
                    ai_coord_score[x, y] = ai_score + neighbor_score
                    # clear the count after scoring a spot
                    self._clear_count()
        max_score_coord = sorted(
            ai_coord_score.items(),
            key=lambda x: x[1],
            reverse=True
        )[0][0]
        return max_score_coord[0], max_score_coord[1]

    # Private
    def _check_col(self, x, y):
        """
        check the board vertically
        Int, Int -> None
        """
        size = self.gc.board.boardsize
        board = copy.deepcopy(self.gc.board.board)
        board[x][y] = AI_STONE
        for x in range(size - FIVE):
            for y in range(size):
                check_human = 0
                check_ai = 0
                for i in range(0, FIVE):
                    if board[x + i][y] == HUMAN_STONE:
                        check_human += 1
                    if board[x + i][y] == AI_STONE:
                        check_ai += 1
                # compare the count of black and white stones
                # then record the number of ai streaks
                if check_ai == FIVE and check_human == 0:
                    self.ai_count["5"] += 1
                elif check_ai == FOUR and check_human == 0:
                    self.ai_count["4"] += 1
                elif check_ai == THREE and check_human == 0:
                    self.ai_count["3"] += 1
                elif check_ai == TWO and check_human == 0:
                    self.ai_count["2"] += 1
                elif check_ai == ONE and check_human == 0:
                    self.ai_count["1"] += 1

    def _check_row(self, x, y):
        """
        check the board horizontally
        Int, Int -> None
        """
        size = self.gc.board.boardsize
        board = copy.deepcopy(self.gc.board.board)
        board[x][y] = AI_STONE
        for y in range(size - FIVE):
            for x in range(size):
                check_human = 0
                check_ai = 0
                for i in range(0, FIVE):
                    if board[x][y + i] == HUMAN_STONE:
                        check_human += 1
                    if board[x][y + i] == AI_STONE:
                        check_ai += 1
                # compare the count of black and white stones
                # then record the number of ai streaks
                if check_ai == FIVE and check_human == 0:
                    self.ai_count["5"] += 1
                elif check_ai == FOUR and check_human == 0:
                    self.ai_count["4"] += 1
                elif check_ai == THREE and check_human == 0:
                    self.ai_count["3"] += 1
                elif check_ai == TWO and check_human == 0:
                    self.ai_count["2"] += 1
                elif check_ai == ONE and check_human == 0:
                    self.ai_count["1"] += 1

    def _check_diag_1(self, x, y):
        """
        check the board from bottom left to top right
        Int, Ints -> None
        """
        size = self.gc.board.boardsize
        board = copy.deepcopy(self.gc.board.board)
        board[x][y] = AI_STONE
        for x in range(size - FIVE + 1):
            for y in range(size - FIVE + 1):
                check_human = 0
                check_ai = 0
                for i in range(0, FIVE):
                    if board[x + i][y + FIVE - 1 - i] == HUMAN_STONE:
                        check_human += 1
                    if board[x + i][y + FIVE - 1 - i] == AI_STONE:
                        check_ai += 1
                # compare the count of black and white stones
                # then record the number of ai streaks
                if check_ai == FIVE and check_human == 0:
                    self.ai_count["5"] += 1
                elif check_ai == FOUR and check_human == 0:
                    self.ai_count["4"] += 1
                elif check_ai == THREE and check_human == 0:
                    self.ai_count["3"] += 1
                elif check_ai == TWO and check_human == 0:
                    self.ai_count["2"] += 1
                elif check_ai == ONE and check_human == 0:
                    self.ai_count["1"] += 1

    def _check_diag_2(self, x, y):
        """
        check the board from top left to bottom right
        Int, Int -> None
        """
        size = self.gc.board.boardsize
        board = copy.deepcopy(self.gc.board.board)
        board[x][y] = AI_STONE
        for x in range(size - FIVE + 1):
            for y in range(size - FIVE + 1):
                check_human = 0
                check_ai = 0
                for i in range(0, FIVE):
                    if board[x + FIVE - 1 - i][y
                                               + FIVE - 1 - i] == HUMAN_STONE:
                        check_human += 1
                    if board[x + FIVE - 1 - i][y
                                               + FIVE - 1 - i] == AI_STONE:
                        check_ai += 1
                # compare the count of black and white stones
                # then record the number of ai streaks
                if check_ai == FIVE and check_human == 0:
                    self.ai_count["5"] += 1
                elif check_ai == FOUR and check_human == 0:
                    self.ai_count["4"] += 1
                elif check_ai == THREE and check_human == 0:
                    self.ai_count["3"] += 1
                elif check_ai == TWO and check_human == 0:
                    self.ai_count["2"] += 1
                elif check_ai == ONE and check_human == 0:
                    self.ai_count["1"] += 1

    def _neighbor_score(self, x, y):
        """
        check the stones around a target spot
        to see if the spot has any neighbor and score it
        Int, Int -> Int
        """
        AI_NBR = 20
        HUMAN_NBR = 10
        size = self.gc.board.boardsize
        board = copy.deepcopy(self.gc.board.board)
        board[x][y] = AI_STONE
        score = 0
        # the conditional is to make sure the index
        # is within the range, as not all spot has
        # eight neighbors
        if x - 1 > 0:
            if board[x - 1][y] == AI_STONE:
                score += AI_NBR
            if board[x - 1][y] == HUMAN_STONE:
                score += HUMAN_NBR
        if x + 1 < size:
            if board[x + 1][y] == AI_STONE:
                score += AI_NBR
            if board[x + 1][y] == HUMAN_STONE:
                score += HUMAN_NBR
        if y - 1 > 0:
            if board[x][y - 1] == AI_STONE:
                score += AI_NBR
            if board[x][y - 1] == HUMAN_STONE:
                score += HUMAN_NBR
        if y + 1 < size:
            if board[x][y + 1] == AI_STONE:
                score += AI_NBR
            if board[x][y + 1] == HUMAN_STONE:
                score += HUMAN_NBR
        if x - 1 > 0 and y - 1 > 0:
            if board[x - 1][y - 1] == AI_STONE:
                score += AI_NBR
            if board[x - 1][y - 1] == HUMAN_STONE:
                score += HUMAN_NBR
        if x - 1 > 0 and y + 1 < size:
            if board[x - 1][y + 1] == AI_STONE:
                score += AI_NBR
            if board[x - 1][y + 1] == HUMAN_STONE:
                score += HUMAN_NBR
        if x + 1 < size and y - 1 > 0:
            if board[x + 1][y - 1] == AI_STONE:
                score += AI_NBR
            if board[x + 1][y - 1] == HUMAN_STONE:
                score += HUMAN_NBR
        if x + 1 < size and y + 1 < size:
            if board[x + 1][y + 1] == AI_STONE:
                score += AI_NBR
            if board[x + 1][y + 1] == HUMAN_STONE:
                score += HUMAN_NBR
        return score

    def _clear_count(self):
        """
        clear the ai streak count
        None -> None
        """
        self.ai_count = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0}
