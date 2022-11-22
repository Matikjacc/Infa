#a = int(input())
lista1 = [1,2,3,4]
lista2 = [9,7,4,8]
a=len(lista1)
def suma(lis):
    sum = 0
    for i in range(0,len(lis)):
        sum+=lis[i]
    return sum
def pier(licz):
    if licz%2 == 0:
        return False
    if licz%3 == 0:
        return False
    for i in range(3, int(pow(licz, 1/2)), 2):
        if licz%i == 0:
            return False
    return True

def pop_sum(lis1, lis2):
    pierwsze = []
    for i in range(a):
        sum = lis1[i]
        p = []
        p.append(lis1[i])
        for j in range(a):
            if j!=i:
                sum+=lis2[j]
                p.append(lis2[j])
        #if pier(sum):
        pierwsze.append(p)
    return pierwsze

def pop1_sum(lis1,lis2):
    ss = []
    for i in range(1, len(lis1)):
        k = 0
        while i+k <= len(lis1):
            p = []
            for j in range(0, k):
                p.append(lis2[j])
            for j in range(k, i+k):
                p.append(lis1[j])
            for j in range(i+k, len(lis2)):
                p.append(lis2[j])
            k+=1
            if(pier(suma(p))):
                ss.append(p)
    return ss
#wejście
#for i in range(a):
#    wej = int(input())
#    lista1[i] = wej
#for i in range(a):
#    wej = int(input())
#    lista1[i] = wej
print(pop1_sum(lista1,lista2))

