n=int(input())
l = list()
for i in range(n):
    l.append(int(input()))
# l = list(set(l))
l.sort()
for i in range(n):
    print(l[i])