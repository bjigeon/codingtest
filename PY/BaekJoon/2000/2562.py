l = []
max = 0
maxcnt = 0
for i in range(1,10):
    n = int(input())
    if(n > max):
        max = n
        maxcnt = i
print(max)
print(maxcnt)  