n = int(input())
def min_iteration(n):
    iter_dict = {}
    iter_dict[1] = 0 
    for i in range(2,n+1):
        if i%3 == 0:
            iter3 = iter_dict[i//3] + 1
        else:
            iter3 = n
        if i%2 == 0:
            iter2 = iter_dict[i//2] + 1
        else:
            iter2 = n
        iter1 = iter_dict[i-1] + 1
        iter_dict[i] = min([iter1,iter2,iter3])
    print(iter_dict[n])
min_iteration(n)