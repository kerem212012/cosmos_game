import time
import curses
import asyncio

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
    coroutines = [blink(canvas, 5, 20),blink(canvas, 5, 18),blink(canvas, 5, 16),blink(canvas, 5, 14),blink(canvas, 5, 12)]
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)
if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
