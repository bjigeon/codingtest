# n = [1]
# n.insert(1,'0')
# print(n)


num = input()
print('num',num)


num = list(num)
if(len(num) == 1):
    num.insert(0,'0')
start = int(num)
print('start',start)
num[0],num[1] = int(num[0]),int(num[1])
print(num)