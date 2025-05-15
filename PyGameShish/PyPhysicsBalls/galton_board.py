import pygame as pg
from random import randrange
import pymunk.pygame_util

from shared import RES, WIDTH, HEIGHT, FPS
from shared import create_ball, create_peg, create_segment

pymunk.pygame_util.positive_y_is_up = False

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 8000
segment_thickness = 10

a, b, c, d = 10, 80, 20, 50
x1, x2, x3, x4 = a, WIDTH // 3 - c, WIDTH // 1.5 + c, WIDTH - a
y1, y2, y3, y4, y5 = b, HEIGHT // 3 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 3 * b
L1, L2, L3= (x1, -150), (x1, y1), (x2, y2)
R1, R2, R3= (x4, -150), (x4, y1), (x3, y2)
B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)

peg_y, step = y4, 60
for i in range(10):
    peg_x = -1.5 * step if i % 2 else -step
    for j in range(WIDTH // step + 2):
        create_peg(peg_x, peg_y, space, 'darkslateblue')
        if i == 9:
            create_segment((peg_x, peg_y + 50), (peg_x, HEIGHT), segment_thickness, space, 'darkslategray')
        peg_x += step
    peg_y += 0.5 * step

platforms = (L1, L2), (L2, L3), (R1, R2), (R2, R3)
for platform in platforms:
    create_segment(*platform, segment_thickness, space, 'darkolivegreen')
create_segment(B1, B2, 20, space, 'darkslategray')

ballz = [([randrange(256) for i in range(3)], create_ball(space)) for j in range(150)]

while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)