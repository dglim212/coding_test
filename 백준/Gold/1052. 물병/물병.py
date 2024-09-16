import math
n,k = map(int,input().split())

answer = 0  
if n/k<1 :
    print(0)
else:
    while bin(n).count('1') >k:
        answer += 1
        n +=1
    print(answer)
        
            
        