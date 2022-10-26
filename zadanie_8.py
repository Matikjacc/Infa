a = int(input())
for i in range(a):
    for j in range(a-(i+1)):
        print(" ", end='')
    for j in range((i*2+1)):
        if i == 0:
            print("X",end='')
        else:
            if j%4 == 1:
                print("o",end='')
            else:
                print("*", end='')
    for j in range(a-(i+1)):
        print(" ", end='')
    print()
for j in range(a-1):
    print(" ", end='')
print("U",end='')
for j in range(a-1):
    print(" ", end='')

