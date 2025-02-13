import random
import asyncio
import curses

async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(random.randint(0, 20)):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(0, 3)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(random.randint(0, 5)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(0, 3)):
            await asyncio.sleep(0)

def get_stars(canvas,row,column):
    symbols = ["*", ".", ":", "+"]
    stars_count = random.randint(50, 200)
    stars = []
    for _ in range(stars_count):
        stars.append(
            blink(canvas, random.randint(0, b=row - 1), random.randint(0, b=column - 1), random.choice(symbols)))
    return stars