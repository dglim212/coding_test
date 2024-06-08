def factorial(n, result=1):
    if n==0:
        print(result)
    else:
        result = result*n
        factorial(n-1,result)
n = int(input())
factorial(n)