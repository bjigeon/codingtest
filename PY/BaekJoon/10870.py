n = int(input())
st = [0,1]
temp = 0
if(n == 1 or n ==2):
    print(1)
    exit()
elif(n == 3):
    print(2)
    exit()
else:
    for i in range(n):
        st.append(st[0]+st[1])
        st.remove(st[0])
print(st[0])