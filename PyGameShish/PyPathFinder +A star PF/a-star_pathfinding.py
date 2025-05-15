import pygame as pg
from heapq import *

from shared import cols, rows
from shared import TILE
from shared import grid
from shared import start
from shared import goal
from shared import get_circle
from shared import get_rect
from shared import get_next_nodes
from shared import heuristic

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()

graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

queue = []

heappush(queue, (0, start))

cost_visited = {start: 0}
visited = {start: None}

bg = pg.image.load('img/z2.png').convert()
bg = pg.transform.scale(bg, (cols * TILE, rows * TILE))

while True:
    sc.blit(bg, (0, 0))

    [pg.draw.rect(sc, pg.Color('black'), get_rect(x, y), 1) for x, y in visited]
    [pg.draw.rect(sc, pg.Color('gray5'), get_rect(*xy)) for _, xy in queue]

    pg.draw.circle(sc, pg.Color('yellow'), *get_circle(*goal))

    if queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            queue = []
            continue

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node

    path_head, path_segment = cur_node, cur_node

    while path_segment:
        pg.draw.circle(sc, pg.Color('brown'), *get_circle(*path_segment))
        path_segment = visited[path_segment]

    # pg.draw.circle(sc, pg.Color('blue'), *get_circle(*start))
    pg.draw.circle(sc, pg.Color('red'), *get_circle(*path_head))

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(10)