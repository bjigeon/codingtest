from cmath import sqrt
import math

# print(52*52)
# print(25*25)
# print(45*45)
# print()
# print(math.sqrt((45**2)+(25**2)))

# d,s,g=map(int,input().split())
# d2=d**2
# s2=s**2
# g2=g**2

# print(52**2)
# print(9**2)
# print(16**2)

# s1=s
# g1=g
# cnt=0
# cnt1=0

# while((s2 + g2) == d2):
#     s2+=s1
#     cnt+=1

#     g2+=g1
#     cnt1+=1

# print(cnt,cnt1)

# d,s,g = map(int,input().split())
# d2=d**2
# s2=s**2
# g2=g**2

# print(d2)
# print(s2)
# print(g2)

# 52**2 = (9+x)**2 + (16+y)**2
# y = x - 27
# x2 - 2x - 1251

d,s,g = map(int,input().split())
print((d**2)*(s/(s+g)**2))
print((d**2)*(g/(s+g)**2))