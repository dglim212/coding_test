n = int(input())
print(2**n -1)
def hanoi(n, before=1, after=3):
    if n==1:
        print(before, after)
    else:
        terminal = 6-before-after
        hanoi(n-1, before, terminal)
        print(before, after)
        hanoi(n-1, terminal, after)
hanoi(n)