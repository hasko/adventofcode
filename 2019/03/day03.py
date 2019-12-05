l1 = []
l2 = []
with open("data.csv", "r") as f:
    l1 = f.readline().split(",")
    l2 = f.readline().split(",")
grid = dict()
(x, y) = (0, 0)
count = 0
for d in l1:
    dir = d[0]
    dist = int(d[1:])
    (xdir, ydir) = (0, 0)
    if dir == "R":
        xdir = 1
    elif dir == "L":
        xdir = -1
    elif dir == "U":
        ydir = 1
    elif dir == "D":
        ydir = -1
    else:
        print("Data error")
        sys.exit(1);
    for i in range(dist):
        count += 1
        (x, y) = (x + xdir, y + ydir)
        if not (x, y) in grid: grid[(x, y)] = count
print(grid)
(x, y) = (0, 0)
count = 0
sol = float("inf")
for d in l2:
    dir = d[0]
    dist = int(d[1:])
    (xdir, ydir) = (0, 0)
    if dir == "R":
        xdir = 1
    elif dir == "L":
        xdir = -1
    elif dir == "U":
        ydir = 1
    elif dir == "D":
        ydir = -1
    else:
        print("Data error")
        sys.exit(1);
    for i in range(dist):
        count += 1
        (x, y) = (x + xdir, y + ydir)
        if (x, y) in grid:
            dd = grid[(x,y)] + count
            if dd < sol: sol = dd
print(sol)
