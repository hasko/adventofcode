import copy
import sys

line = ""
with open("data.txt", "r") as file:
    line = file.readline()
mem = [int(code) for code in line.split(",")]
# Part 1
# mem[1] = 12
# mem[2] = 2
initMem = copy.deepcopy(mem)
f = [None, lambda x, y : x + y, lambda x, y : x * y]
for noun in range(0, 100):
    for verb in range(0, 100):
        mem = copy.deepcopy(initMem)
        mem[1] = noun
        mem[2] = verb
        for i in range(0, len(mem), 4):
            if mem[i] == 99:
                break
            try:
                mem[mem[i+3]] = f[mem[i]](mem[mem[i+1]], mem[mem[i+2]])
            except (IndexError, TypeError) as err:
                print(str(noun) + ", " + str(verb) + " produced an error: " + str(err))
                mem[0] = 0 # Make sure we don't accidentally leave the desired result.
                break
# Part 1
#        print(mem[0])
        if mem[0] == 19690720:
            print(100 * noun + verb)
            sys.exit()
