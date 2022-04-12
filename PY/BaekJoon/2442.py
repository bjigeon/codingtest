n = int(input())
cnt = 1
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(cnt):
        print('*',end='')
    cnt +=2
    print()
    