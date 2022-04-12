from random import randrange

max = 0
abc = list(map(int,input().split()))
print(abc)
# for i in range(len(abc)):
#     if abc[i] > max:
#         max = abc[i]
# print(max)
print(max(abc))