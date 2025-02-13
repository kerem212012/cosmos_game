import random
import time

from animations.fire_animation import *
from animations.stars import blink,get_stars
from animations.starship import animate_spaceship

TIC_TIMEOUT = 0.1


def draw(canvas):
    curses.curs_set(False)
    row, column = curses.window.getmaxyx(canvas)
    stars = get_stars(canvas,row,column)
    ship = animate_spaceship(canvas,row/2-3,column/2)
    coroutines = [*stars,ship]



    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
