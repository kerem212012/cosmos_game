import asyncio
from itertools import cycle

from animations.curses_tools import draw_frame


def twice_cycle(iterable):
    for ship in cycle(iterable):
        for _ in range(2):
            yield ship


def get_rockets():
    with open("rocket/rocket_frame_1.txt", "r") as f1:
        frame_1 = f1.read()
    with open("rocket/rocket_frame_2.txt", "r") as f2:
        frame_2 = f2.read()
    rockets = [frame_1, frame_2]
    return rockets


async def animate_spaceship(canvas, row, column):
    for frame in twice_cycle(get_rockets()):
        draw_frame(canvas, row, column, frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, frame, negative=True)
