# from collections import deque
# num = input()
# # print(num)
# num = deque(list(num))
# if(len(num) == 1):
#     num.insert(0,'0')
# num[0],num[1] = int(num[0]),int(num[1])
# start = int(''.join(map(str, num)))
# num.append(num[0] + num[1])
# cnt = 1
# global sum
# sum = 0

# def count():
#     global sum
#     num.remove(num[0])
#     sum = int(str(num[0]) + str(num[1]))
        
#     if(num[0] + num[1] > 10):
#         num.append(int(list(str(num[0] + num[1]))[1]))
#     else:
#         num.append(num[0] + num[1])

# count()
# while True:
#     count()
#     cnt += 1
#     if(sum == start):
#         print(cnt)
#         break



from collections import deque
global sum
cnt = 1
start = int(input())
num = deque(str(start))
print(num)

if(start == 0):
    print(1)
    exit()
elif( start <= 10):
    num.appendleft(str(0))
print(num)
print('num[0] : ',num[0])

num.append(int(num[0])+int(num[1]))

def count():
    num.popleft()
    int(num[0])
    int(num[1])
    num.append(num[0]+num[1])
    if(num[0] + num[1] > 10):
        num.append(int(list(num[0] + num[1])[1]))
    else:
        num.append(num[0] + num[1])


count()
while True:
    cnt+=1
    if(sum==start):
        print(cnt)
        break
