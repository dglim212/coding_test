a,b,c = map(int,input().split())
if (a-b)*(b-c)*(c-a) == 0:
    if (a == b):
        score = 1000 + 100*a
        if (b == c):
            score = score*10
    else:
        score = 1000 + 100*c
else:
    score = max([a,b,c])*100
print(score)