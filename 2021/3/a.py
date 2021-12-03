import sys

counts = None
lines = 0
with open(sys.argv[1]) as f:
    while len(line := f.readline().strip()) > 0:
        digits = [char for char in line]
        lines += 1
        if counts is None:
            counts = [0] * len(digits)
        for i, d in enumerate(digits):
            counts[i] += int(d)


gamma = 0
epsilon = 0
lines /= 2
while len(counts) > 0:
    gamma <<= 1
    epsilon <<= 1
    if counts.pop(0) > lines:
        gamma += 1
    else:
        epsilon += 1

print(f"Gamma: {gamma}, Epsilon: {epsilon}, Power: {gamma * epsilon}")
