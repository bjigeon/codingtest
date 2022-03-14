k = int(input())
cnt = 0
if(k%5 == 0):
    print(k//5)
    print(1)
    

elif(k%5 != 0 and k%3 != 0):
    print(-1)
    print(3)

elif(k%3 == 0):
    print(k//3)
    print(4)

# else((k%5) // 3 + k//5 < k//3):
else:
    print((k%5) // 3 + k//5)
    print(2)


k = int(input())
cnt = 0
if(k%5 == 0):
    print(k//5)
elif(k%5 != 0 and k%3 != 0):
    print(-1)
elif(k%3 == 0):
    print(k//3)
else:
    print((k%5) // 3 + k//5)