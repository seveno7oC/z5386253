#functions
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

res = qan_tic()
print(res)

#Only print once because print after return
def qan_tic():
    tic = "QAN.AX"
    return tic
    print(tic)

res = qan_tic()
print(res)


# No return print none
def qan_tic():
    tic = "QAN.AX"
    print(tic)


res = qan_tic()
print(res)


#
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

print(qan_tic)

# will be error
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

print(tic)

#Scopes and namespace
def qan_tic():
    tic = "QAN.AX"          #<--- local
    print(tic)
    return tic

tic = "WES.AX"          #<--- global
print(tic)       #give WES.AX
qan_tic()        #give QAN.AX

#
def qan_tic():
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()

#Parameters

#Comprehensions

#Modules

#
def add(a,b):
    """Returns the sum of two numbers- FINTECH DEMO"""
    return a+b

#Docstring styles