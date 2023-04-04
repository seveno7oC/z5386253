numbers = [0,1,1,2,5,6,8,2,4,6,8]
def i(lis):
    intergers = []
    for z in numbers:
        if z % 2 == 0:
            intergers.append(z)
    return intergers

print(i(lst))


#example
numbers = [0,1,1,2,5,6,8,2,4,6,8]
result = list({i for i in numbers if i % 2 == 0})
print(result)

#
numbers = [0,1,1,2,5,6,8,2,4,6,8]
result = [i for i in set(numbers) if 1 % 2 == 0]
result.sort()
print(result)