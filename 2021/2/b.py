import sys

pos = 0
aim = 0
depth = 0
with open(sys.argv[1]) as f:

    countIncrease = 0
    previous = None
    while line := f.readline().split():
        cmd = line[0]
        value = int(line[1])
        if cmd == "forward":
            pos += value
            depth += aim * value
        elif cmd == "down":
            aim += value
        elif cmd == "up":
            aim -= value
        else:
            print("Unknown command: {cmd} {value}")

print(f"Final position: {pos}, depth: {depth}, result: {pos * depth}")
