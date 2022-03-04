for _ in range(int(input())):
    num, st = input().split()
    for i in range(len(st)):
        print(st[i]*int(num),end="")
    print()
