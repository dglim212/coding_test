import sys
def cantor(n):
    if n==0:
        return '-'
    else:
        blank = ' '*(3**(n-1))
        cantor_small = cantor(n-1)
        return cantor_small + blank + cantor_small
data = sys.stdin.read().strip()
line = map(int, data.split())
for n in line:
    print(cantor(n))