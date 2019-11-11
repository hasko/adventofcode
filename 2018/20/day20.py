import sys

mode = sys.argv[2]

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    expression = ""
    while True:
        l = lines.pop(0).strip()
        expression += l
        if l[-1] == "$": break
    if mode == "test":
        l = lines.pop(0).strip()
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

def flood():
    dist = {}
    queue = [(0, 0)]
    d = 0
    mem = []
    while True:
        new_queue = []
        while len(queue) > 0:
            print(str(d) + ": " + str(len(queue)))
            p = queue.pop(0)
            if p not in mem:
                mem.append(p)
                dist[p] = d
                if (p[0] - 1, p[1]) in maze_dict:
                    new_queue.append((p[0] - 2, p[1]))
                if (p[0] + 1, p[1]) in maze_dict:
                    new_queue.append((p[0] + 2, p[1]))
                if (p[0], p[1] - 1) in maze_dict:
                    new_queue.append((p[0], p[1] - 2))
                if (p[0], p[1] + 1) in maze_dict:
                    new_queue.append((p[0], p[1] + 2))
        if len(new_queue) == 0: break
        queue = new_queue
        d += 1
    return dist

dist = flood()
max_dist = max([dist[p] for p in dist])
if mode == "test":
    if solution == max_dist:
        print("Distance test passed")
    else:
        print("Distance test failed")
print("Maximum distance: " + str(max_dist))
