import random
while True:
    a = float(input())
    b = float(input())
    c = input()
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    elif c == "#":
        print(pow(a,1/b))
    elif c == "^":
        print(pow(a, b))
    elif c == "x":
        print(random.randint(int(a),int(b)))
    elif c == "e":
        exit()
    print("Czy chcesz wprowadzić nowe dane?")
    t = input()
    if t == "N":
        exit()
