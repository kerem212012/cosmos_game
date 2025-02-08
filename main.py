import time
import curses
import asyncio
import random


TIC_TIMEOUT = 0.1
async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed

async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(random.randint(0,20)):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(0,3)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(random.randint(0,5)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(0,3)):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    symbols = ["*",".",":","+"]
    stars_count = random.randint(50,200)
    row,column = curses.window.getmaxyx(canvas)
    coroutines = []
    for _ in range(stars_count):
        coroutines.append(blink(canvas,random.randint(0, b=row-1),random.randint(0,b=column-1),random.choice(symbols)))
    coroutines.append(fire(canvas,row/2,column/2))
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
