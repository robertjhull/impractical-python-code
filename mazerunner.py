from random import randint
import pprint

pp = pprint.PrettyPrinter(indent=4,width=100)

maze_init = [
    [2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2],
]

def direction():
    x = randint(0,3)
    if x == 0:
        return "right"
    if x == 1:
        return "down"
    if x == 2:
        return "left"
    if x == 3:
        return "up"

maze = maze_init

def run():
    y = 1
    x = 9
    stuck = 0
    while True:
        current_location = maze[y][x]
        if maze[y][x] == 3:
            print("finished")
            pp.pprint(maze)
            return False
        if stuck == 100:
            print("dead end")
            pp.pprint(maze)
            return False
        where = direction()
        if where == "right":
            if maze[y][x+1] == 1:
                maze[y][x+1] = 0
                x += 1
                pp.pprint(maze)
        if where == "down":
            if maze[y+1][x] == 1:
                print("down")
                maze[y+1][x] = 0
                y += 1
                pp.pprint(maze)
        if where == "left":
            if maze[y][x-1] == 1:
                print("left")
                maze[y][x-1] = 0
                x -= 1
                pp.pprint(maze)
        if where == "top":
            if maze[y-1][x] == 1:
                print("top")
                maze[y-1][x] = 0
                y -= 1
                pp.pprint(maze)
        else:
            stuck += 1

run()
