num = input()
# print(num)
num = list(num)
if(len(num) == 1):
    num.insert(0,'0')
num[0],num[1] = int(num[0]),int(num[1])
start = int(num)
num.append(num[0] + num[1])
cnt = 1
global sum
sum = 0
print('num :',num)

def count():
    global sum
    num.remove(num[0])
    sum = int(str(num[0]) + str(num[1]))
    print('sum :',sum)
    if(sum == start):
        print('일치')
        
    if(num[0] + num[1] > 10):
        num.append(int(list(str(num[0] + num[1]))[1]))
    else:
        num.append(num[0] + num[1])
    print(num)

count()
while True:
    count()
    cnt += 1
    if(sum == start):
        print(cnt)
        break