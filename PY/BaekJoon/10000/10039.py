s=list()
sum=0
for i in range(5):
    s.append(int(input()))
    if s[i] < 40:
        s[i] = 40
    sum+=s[i]
print(sum//5)