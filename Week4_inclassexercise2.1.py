lst = [2,3,10,14,20,21,25,13,15]
def i(lis):
    number = []
    for a in lst:
        if a*a > 150:
            number.append(a**2)
    return number

print(i(lst))


#example
lst = [2,3,10,14,20,21,25,13,15]
new_lst = [x**2 for x in lst if x**2>150]
print(new_lst)