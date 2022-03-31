for i in range(int(input())):
    st = []
    cnt = 0
    sum = 0
    
    st = input().split()
    for i in range(int(st[0])):
        sum += int(st[i+1])

    avg = sum/int(st[0])

    for i in range(int(st[0])):
        if int(st[i+1]) > avg:
            cnt += 1
    print("%.3f%%" % (cnt / int(st[0]) * 100.0))