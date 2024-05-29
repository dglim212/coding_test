def turret():
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if (d==0) & (r1==r2):
        print(-1)
    elif (r1+r2<d) | (abs(r1-r2)>d) :
        print(0)
    elif (r1+r2>d) & (abs(r1-r2)<d):
        print(2)
    elif (r1+r2==d) | (abs(r1-r2) == d):
        print(1)
n = int(input())
for i in range(n):
    turret()