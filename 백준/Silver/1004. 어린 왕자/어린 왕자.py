def question(x1,y1, x2,y2, x,y,r):
    valid = False
    if ((x-x1)**2 + (y-y1)**2 - r**2)*((x-x2)**2 + (y-y2)**2 - r**2)<0:
        valid = True
    return valid
n = int(input())
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    n_test = int(input())
    answer = 0
    for j in range(n_test):
        x_test,y_test,r = map(int, input().split())
        if question(x1,y1,x2,y2,x_test,y_test,r):
            answer+=1
    print(answer)
        
        