# from collections import deque

# num = [0] * 3
# print(num)
# n = int(input())
# num[0],num[1] = n//10, n%10 

# start = num[0] + num[1]
# num[2] = num[0] + num[1]
# print(num[2])
# num = deque(num)

# print('start :',start)
# cnt = 0
# while(start == num[2]):
#     cnt += 1
#     num.popleft()
#     print(num)
#     if(num[2] >= 10):
#         if(num[2]//10 == 1):
#             num[2] == 0
#         num[2] = num[2]//10    
#     num[2] = num[0] + num[1]




# num = [0] * 3
# print(num)
# n = int(input())
# num[0],num[1] = n//10, n%10 

# start = num[0] + num[1]
# num[2] = num[0] + num[1]
# print('start :',start)
# print('num[2] :',num[2])
# cnt = 0
# while(start == num[2]):
#     cnt += 1
#     num.remove(num[0])
#     print('num :',num)
#     if(num[2] > 10):
#         num[2] %= 10
#     num[2] = num[0] + num[1]
# print(cnt)

num = [0] * 3
print(num)
n = int(input())
num[0],num[1] = n//10, n%10
num[2] = num[0] + num[1]
print('num[2] :',num[2])
cnt = 0
for i in range(10):
    cnt += 1
    num.remove(num[0])
    print('num :',num)
    num.append(num[0] + num[1])
    if(num[2] > 10):
        num[2] %= 10
print(cnt)