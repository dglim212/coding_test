def answer(n:int):
    dict={}
    dict[1] = 1
    dict[2] = 2
    dict[3] = 4
    for i in range(4,n+1):
        dict[i] = dict[i-1] + dict[i-2] + dict[i-3]
    print(dict[n])
test_numb = int(input())
for i in range(test_numb):
    answer(int(input()))
    
