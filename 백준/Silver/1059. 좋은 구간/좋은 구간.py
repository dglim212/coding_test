L = int(input())
numbers = map(int,input().split())
n = int(input())
min_set = []
max_set = []
for number in numbers:
    if number <= n:
        min_set.append(number)
    if number >= n:
        max_set.append(number)
if len(min_set) == 0:
    min_set.append(0)
answer = (n-max(min_set))*(min(max_set)-n) -1
if answer<0:
    answer=0
print(answer)
