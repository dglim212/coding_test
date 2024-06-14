import sys
n,k = map(int,sys.stdin.readline().split())
def next_step(n,n_mini,digit_mini,k):
    temp = n_mini*digit_mini + n
    return(temp%k)
    
n_mini = n%k
digit = len(str(n))
digit_mini = pow(10,digit,k)
remainers = set()
for i in range(1,k+1):
    if n_mini == 0:
        print(len(remainers)+1)
        break
    elif n_mini in remainers:
        print(-1)
        break
    else:
        remainers.add(n_mini)
        n_mini = next_step(n,n_mini,digit_mini,k)
