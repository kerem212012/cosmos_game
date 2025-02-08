import time
import curses
import asyncio
import random


TIC_TIMEOUT = 0.1
async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(20):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    symbols = ["*",".",":","+"]
    stars_count = random.randint(50,200)
    row,column = curses.window.getmaxyx(canvas)
    coroutines = []
    for _ in range(stars_count):
        coroutines.append(blink(canvas,random.randint(1, b=row-2),random.randint(1,b=column-2),random.choice(symbols)))
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)
if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
