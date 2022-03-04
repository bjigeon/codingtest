n = int(input())
for i in range(n):
    for j in range(n):
        if(i == 0 or i == n):
            for k in range(n):
                print('*',end='')
            print()