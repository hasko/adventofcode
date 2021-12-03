import sys

def countOnes(numbers):
    counts = [0] * len(numbers[0])
    for digits in numbers:
        for i, d in enumerate(digits):
            counts[i] += int(d)
    return counts


with open(sys.argv[1]) as f:
    lines = f.readlines()
lines = [[char for char in line.strip()] for line in lines]

bits = len(lines[0])

numbers = lines
for i in range(bits):
    if len(numbers) <= 1: break
    counts = countOnes(numbers)
    cut = len(numbers) / 2
    numbers = [num for num in numbers if num[i] == ("1" if counts[i] >= cut else "0")]
oxy = int("".join(numbers[0]), 2)

numbers = lines
for i in range(bits):
    if len(numbers) <= 1: break
    counts = countOnes(numbers)
    cut = len(numbers) / 2
    numbers = [num for num in numbers if num[i] == ("1" if counts[i] < cut else "0")]
scrub = int("".join(numbers[0]), 2)

print(f"Oxy: {oxy}, scrub: {scrub}, life support: {oxy * scrub}")
