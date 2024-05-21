score = int(input())
if score >= 60:
    print('AABCD'[10-(score//10)])
else:
    print('F')