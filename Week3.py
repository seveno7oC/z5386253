#
var1 = ['a']
var2 = ['a']
var3 = ['a']
var4 = ['a']

#
lst1 = ['a']
print(f'This is lst1:{lst1}')

lst2 = ['b', lst1]
print(f'This is lst2:{lst2}')

#
happy = False
if happy is True:
    print("I'm happy")
print("This will print regardless of the value of happy")

happy = True
if happy is True:
    print("I'm happy")
print("This will print regardless of the value of happy")


#
happy = 10
if happy:
    print("im happy")
#
var1 = "a"
var2 = "a"
var3 = ["a"]
var4 = ["a"]

var1 == var2 #true
var1 is var2
#false

var3 == var4 #true
var3 is var4 #false


#
a = 0
b = True
if a != 0:
    print("s id non-zero")
elif b is True:
    print("b is true")
elif a < 0 and b is True:
    print("a is negative and b is true")
else:
    print("None of the conditions above hold")

a = -1
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is true")
elif a < 0 and b is True:
    print("a is negative and b is true")
else:
    print("None of the conditions above hold")

#
happy = True
if happy is True:
    pass

#input function
name = input("Who are you?")
print(f"Welcome to the class,{name}")


#loops
letter_lst = ["a","b","c","d"]
for letter in letter_lst:
    print(letter)

#
d = {
    "Beauty": True,
    "truth": True,
    "red": 100000,
    5: "fingers"
}
for val in d.values():
    print(val)

for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")

key,value = key_value_tuple
print(f"KEY:{key} VALUE:{value}")

#
for even in range(0,10,2):
    print(f"even is now {even}")


#while loop
the_sum = 0
for i in range(1,101):
    the_sum = the_sum + i
    i = i+1
print(the_sum)

#the continue statement
letters = ['a','b','c','d','e']


#
for even in range(0,10,2):
    print(even)
    if even > 2:
        break


for odd in range(1,10,2):
    for even in range(0,10,2):
        if even >2:
            break
        print(even,odd)


#
for even in range(0,10,2):
    print(even)
    if even > 2:
        continue


for even in range(0,10,2):
    if even > 2:
        continue
        print(even)

for even in range(0, 10, 2):
    if even > 2:
        continue
print(even)