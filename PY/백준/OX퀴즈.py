for _ in range(int(input())):
    sum = 0
    sc = 0
    for i in input():
        if i == "O":
            sc += 1
        else:
            sc = 0
        sum+=sc
    print(sum)
 