import csv
import math

def calc(m):
    return max(math.floor(m / 3) - 2, 0)

with open("data.csv", "r") as csvfile:
    data = csv.reader(csvfile);
    total = 0
    for row in data:
        mass = int(row[0])
        while True:
            fuel = calc(mass)
            if fuel == 0:
                break;
            total += fuel
            mass = fuel
    print("Total: " + str(total))
