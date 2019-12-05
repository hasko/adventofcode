import re

double = re.compile(r"(.)(\1+)")

def test(s):
    for j in range(5):
        if s[j + 1] < s[j]: return False
    for m in re.finditer(double, s):
        if len(m.group(2)) == 1: return True
    return False

count = 0
for i in range(372304, 847060 + 1):
    if test(str(i)):
        count += 1
        print(i, end=", ")

print(count)
