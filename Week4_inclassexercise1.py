l = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,19,30,31]
def e(lis):
    evennum=[]
    for n in l:
        if n % 2 == 0:
            evennum.append(n)
    return evennum

e(l)
print(e(l))
