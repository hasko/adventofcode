import sys

mode = sys.argv[2]

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    l = lines.pop(0).strip()
    expression = ""
    while len(l) > 0:
        expression += l
        l = lines.pop(0).strip()
    if mode == "test":
        maze_sol = []
        l = lines.pop(0).strip()
        while len(l) > 0:
            maze_sol.append(l)
            l = lines.pop(0).strip()
        l = lines.pop(0).strip()
        solution = int(l)

maze_dict = {}

def expand(index, pos_init):
    pos = pos_init
    next = expression[index]
    while next is not "$":
        print(str(index) + " " + next)
        if next == "^":
            index += 1
        elif next is "N":
            maze_dict[(pos[0] - 1, pos[1])] = "-"
            maze_dict[(pos[0] - 2, pos[1])] = "."
            pos = (pos[0] - 2, pos[1])
            index += 1
        elif next is "S":
            maze_dict[(pos[0] + 1, pos[1])] = "-"
            maze_dict[(pos[0] + 2, pos[1])] = "."
            pos = (pos[0] + 2, pos[1])
            index += 1
        elif next is "W":
            maze_dict[(pos[0], pos[1] - 1)] = "|"
            maze_dict[(pos[0], pos[1] - 2)] = "."
            pos = (pos[0], pos[1] - 2)
            index += 1
        elif next is "E":
            maze_dict[(pos[0], pos[1] + 1)] = "|"
            maze_dict[(pos[0], pos[1] + 2)] = "."
            pos = (pos[0], pos[1] + 2)
            index += 1
        elif next is "(":
            (index, pos) = expand(index + 1, pos)
        elif next is ")":
            return (index + 1, pos_init)
        elif next is "|":
            pos = pos_init
            index += 1
        next = expression[index]

def flatten():
    yy = [p[0] for p in maze_dict]
    xx = [p[1] for p in maze_dict]
    xMin = min(xx)
    xMax = max(xx)
    yMin = min(yy)
    yMax = max(yy)
    xSize = xMax - xMin + 3
    ySize = yMax - yMin + 3
    maze = ["#"] * xSize * ySize
    for x in range(xSize):
        for y in range(ySize):
            coords = (y + yMin - 1, x + xMin - 1)
            if coords in maze_dict:
                maze[y * xSize + x] = maze_dict[coords]
    res = []
    for l in range(ySize):
        res.append("".join(maze[l * xSize : l * xSize + xSize]))
        print("".join(maze[l * xSize : l * xSize + xSize]))
    return res

maze_dict[(0 , 0)] = "X"
expand(0, (0, 0))
if mode == "test":
    maze = flatten()
    for i, l in enumerate(maze_sol):
        if l != maze[i]:
            print("Wrong maze")
            exit()
    print("Maze test passed")
