# n = int(input())
# re = []
# for i in range(n):
#     buk = list(map(int,input().split()))
#     re.extend(buk)
#     bba = int(input())
#     for j in range(bba):
#         buk.remove(buk(len(buk)))
    
# print(re)

# re = []
# buk = list(map(int,input().split()))
# re.extend(buk)
# print(re)
# list.remove(5)


# re = []
# buk = list(map(int,input().split()))
# re.extend(buk)
# print(re)
# bba = int(input())
# for j in range(bba):
#     re.remove(buk[len(buk)])
    
# print(re)

#바운드 볼 ############################################################################

# re=[]
# n=list(map(int,input().split()))
# print(n)
# l = len(n)
# print(l)
# for i in range(l):
#     if (n[i] < 0):
#         re.append(n[i])
#         n.remove(n[i])

# re += n
# print(re)

# re=[]
# n=list(map(int,input().split()))
# print(n)
# l = len(n)
# print(l)
# for i in range(l):
#     if (n[i] < 0):
#         re.extend(n[i])
#         n.remove(n[i])


arr=list(map(int,input().split()))
e = [i for i in arr if i < 0]
y = [i for i in arr if i > 0]
re = e+y
print(re)