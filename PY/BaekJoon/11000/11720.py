n = int(input())
num = int(input())
l = list(str(num))
if len(l) != n:
    exit()

sum = 0
for i in range(len(l)):
    sum += int(l[i])

print(sum)