from os import name
from game_controller import GameController

CONTINUE = -1
HUMAN_WIN = 1
PIXEL_WIDTH = 500
SIZE = 15
BORDERRATIO = 0.1
BORDER = PIXEL_WIDTH * BORDERRATIO
BLOCK = PIXEL_WIDTH - 2 * BORDER
UNIT_WIDTH = BLOCK / (SIZE - 1)
BG_COLOR = (140, 100, 0)
ELLIPSE_SIZE = 0.5 * UNIT_WIDTH

field = (PIXEL_WIDTH, PIXEL_WIDTH)
gc = GameController(SIZE)


def setup():
    """
    Setup the board background
    """
    size(*field)
    strokeWeight(3)
    background(*BG_COLOR)
    fill(140, 100, 0)
    rect(BORDER, BORDER, BLOCK, BLOCK)
    for i in range(SIZE):
        line(BORDER + i * UNIT_WIDTH, BORDER, BORDER + i * UNIT_WIDTH,
             PIXEL_WIDTH - BORDER)
        line(BORDER, BORDER + i * UNIT_WIDTH, PIXEL_WIDTH - BORDER, BORDER
             + i * UNIT_WIDTH)


def draw():
    """
    Draw the enviroment and stones
    """
    if gc.game_reuslt() == CONTINUE:
        if gc.cur_step % 2 == 0:
            gc.allowMousePress = True
        else:
            delay(2000)  # delay 2 seconds
            gc.ai_drop_stone(BORDER, UNIT_WIDTH)
    else:
        gc.end_text()
        if gc.game_reuslt() == HUMAN_WIN:
            answer = input('enter your name')
            if answer:
                print('Hi ' + answer)
            elif answer == '':
                print('[empty string]')
            else:
                print(answer)
            gc.player_score(answer)
        exit()


def mousePressed():
    """
    1. Drop the stone to the nearest when mouse is pressed
    2. Auto-switch the color when there are two human players
    3. Display end text in terminal when the board is full
    """
    gc.human_drop_stone(mouseX, mouseY, BORDER, PIXEL_WIDTH, UNIT_WIDTH)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
