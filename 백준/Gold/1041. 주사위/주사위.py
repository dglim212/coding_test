n = int(input())
a,b,c,d,e,f = map(int,input().split())
dim1 = [a,b,c,d,e,f]
dim2 = [a+b, a+c, a+d, a+e, b+c, b+d, b+f , c+e, c+f,d+e, d+f, e+f]
dim3 = [a+b+c, a+b+d, a+c+e, a+d+e, b+c+f, b+d+f, c+e+f, d+e+f]
if n >1:
    min_1dim = min(dim1)
    num_1dim = 5*((n-2)**2) + (n-2)*4
    min_2dim = min(dim2)
    num_2dim = (n-2)*4 + (n-1)*4
    min_3dim = min(dim3)
    num_3dim = 4
    print(min_1dim * num_1dim + min_2dim * num_2dim + min_3dim * num_3dim ) 
elif n == 1:
    print(sum(dim1) - max(dim1))