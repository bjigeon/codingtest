sum = 0
a = int(input())
l = input().split()
for i in range(a):
    l[i] = int(l[i])
m = max(l)
for i in range(a):
    sum += l[i]/m*100
print(sum/a)
