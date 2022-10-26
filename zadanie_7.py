a = int(input())
b = int(input())
if abs(b-a) > 20:
    for i in range(int((b+a)/2)-3,int((b+a)/2)+4):
        if i != (a+b)/2:
            print(i)
else:
    i = a
    while i <= b:
        print(i)
        i+=1
