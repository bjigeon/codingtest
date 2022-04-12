# 최대공약수
# n,m=map(int,input().split())
# for i in range(min(n,m),0,-1):
#     if n % i == 0 and m % i == 0:
#         print(i)
#         break

# 최소공배수
# n,m=map(int,input().split())
# for i in range(max(n,m),(n*m)+1):
#     if i%n == 0 and i%m==0:
#         print(i)
#         break

# 함수
# from math import gcd
# n,m=map(int,input().split())
# print(gcd(n,m)) #최대공약수
# print(n*m // gcd(n,m)) #최대공배수

# def 최대공약수(a,b):
#     if b == 0:
#         return a
#     else:
#         return 최대공약수(b,a%b)

# a,b=map(int,input().split())
# print(최대공약수(a,b))