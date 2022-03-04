import math

# print(52*52)
# print(25*25)
# print(45*45)
# print()
# print(math.sqrt((45**2)+(25**2)))

d,s,g=map(int,input().split())
d2=d**2
s2=s**2
g2=g**2

print(52**2)
print(9**2)
print(16**2)

s1=s
g1=g
cnt=0
cnt1=0

while((s2 + g2) == d2):
    s2+=s1
    cnt+=1

    g2+=g1
    cnt1+=1

print(cnt,cnt1)