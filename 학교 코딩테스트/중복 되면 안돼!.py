n=list(map(int,input().split()))
n.sort()
n = list(set(n))
for i in range(len(n)):
    print(n[i], end=' ')