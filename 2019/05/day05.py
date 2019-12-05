import copy
import sys

def read(addr, mode):
    res = None
    try:
        res = mem[addr]
        if mode == 0: res = mem[res]
        if mode == 0:
            print(f"({mem[addr]})->{res}", end="")
        else:
            print(f"{mem[addr]}", end="")
    except IndexError as err:
        print(str(err) + ", mode=" + str(mode) + ", IP=" + str(addr))
        raise
    return res

def print_codes(addr, n):
    s = ""
    for i in range(n):
        s += str(mem[addr + i]) + " "
    s += " " * (30 - len(s))
    print(s, end="")

line = ""
with open("data.csv", "r") as file:
    line = file.readline()
mem = [int(code) for code in line.split(",")]
input = [5]
output = []
f = [None, lambda x, y : x + y, lambda x, y : x * y, None, None, None, None, lambda x, y : 1 if x < y else 0, lambda x, y: 1 if x == y else 0]
ip = 0
while True:
    print(f"{ip}\t", end="")
    instr = mem[ip]
    op_code = instr % 100
    mode_a = (instr // 100) % 10
    mode_b = (instr // 1000) % 10
    if op_code == 99:
        print_codes(ip, 1)
        print(f"HALT")
        ip += 1
        break
    elif op_code == 1 or op_code == 2 or op_code == 7 or op_code == 8:
        print_codes(ip, 4)
        print(["ADD", "MUL", None, None, None, None, "LES", "EQU"][op_code - 1], end=" ")
        a = read(ip + 1, mode_a)
        print(", ", end="")
        b = read(ip + 2, mode_b)
        c = mem[ip + 3]
        mem[c] = f[op_code](a, b)
        print(f", ({c})<-{mem[c]}")
        ip += 4
    elif op_code == 3:
        print_codes(ip, 2)
        print(f"IN ", end="")
        a = read(ip + 1, 1)
        mem[a] = input.pop()
        print(f"->{mem[a]}")
        ip += 2
    elif op_code == 4:
        print_codes(ip, 2)
        print(f"OUT ", end="")
        a = read(ip + 1, 1)
        output.append(mem[a])
        print()
        ip += 2
    elif op_code == 5 or op_code == 6:
        print_codes(ip, 3)
        print(["JPT ", "JPF "][op_code - 5], end="")
        a = read(ip + 1, mode_a)
        print(", ", end="")
        b = read(ip + 2, mode_b)
        print()
        if (a != 0 and op_code == 5) or (a == 0 and op_code == 6):
            ip = b
        else:
            ip += 3
    else:
        print("Invalid opcode")
        break


print(output)
